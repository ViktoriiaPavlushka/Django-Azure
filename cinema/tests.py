from django.test import TestCase , Client
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, time
from .models import User, Director, Hall, Film, Session
from .repositories import (
    UserRepository, DirectorRepository, HallRepository, FilmStatisticsRepository,
    SessionStatisticsRepository
)

class UserRepositoryTest(TestCase):
    def setUp(self):
        self.user_data = {
            'name': 'John',
            'lastName': 'Doe',
            'yearOfBirth': '1990-01-01',
            'phoneNumber': '1234567890'
        }
        self.user = User.objects.create(**self.user_data)

    def test_add_user(self):
        user_data = {
            'name': 'Alice',
            'lastName': 'Smith',
            'yearOfBirth': '1990-01-01',
            'phoneNumber': '0987654321'
        }
        UserRepository.add(user_data)
        self.assertTrue(User.objects.filter(phoneNumber='0987654321').exists())

    def test_get_by_phone_number(self):
        user = UserRepository.getByPhoneNumber('1234567890')
        self.assertEqual(user.name, 'John')

    def test_get_by_id(self):
        user = UserRepository.getByID(self.user.userID)
        self.assertEqual(user.phoneNumber, '1234567890')

    def test_delete_user(self):
        UserRepository.delete(self.user.userID)
        self.assertFalse(User.objects.filter(userID=self.user.userID).exists())

    def test_update_user(self):
        updated_data = {'name': 'Johnny'}
        UserRepository.update(self.user.userID, updated_data)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, 'Johnny')


class DirectorRepositoryTest(TestCase):
    def setUp(self):
        self.director = Director.objects.create(name='Christopher', lastName='Nolan', yearOfBirth= '1990-01-01')

    def test_add_director(self):
        director_data = {'name': 'Quentin', 'lastName': 'Tarantino', 'yearOfBirth': '1980-01-01'}
        DirectorRepository.add(director_data)
        self.assertTrue(Director.objects.filter(name='Quentin', lastName='Tarantino').exists())

    def test_get_by_id(self):
        director = DirectorRepository.getByID(self.director.directorID)
        self.assertEqual(director.name, 'Christopher')
        self.assertEqual(director.lastName, 'Nolan')


class HallRepositoryTest(TestCase):
    def setUp(self):
        self.hall = Hall.objects.create(numberOfSeats=100)

    def test_get_hall_by_id(self):
        hall = HallRepository.getByID(self.hall.hallID)
        self.assertEqual(hall.numberOfSeats, 100)

    def test_add_hall(self):
        hall_data = { 'numberOfSeats': 50}
        HallRepository.add(hall_data)
        self.assertTrue(Hall.objects.filter(numberOfSeats = 50).exists())


class FilmStatisticsRepositoryTest(TestCase):
    def setUp(self):
        self.director1 = Director.objects.create(name='Director', lastName='One', yearOfBirth='1980-01-01')
        self.director2 = Director.objects.create(name='Director', lastName='Two', yearOfBirth='1985-01-01')

        self.film1 = Film.objects.create(name='Film 1', year=2020, directorID=self.director1)
        self.film2 = Film.objects.create(name='Film 2', year=2021, directorID=self.director2)

    def test_get_film_statistics(self):
        stats = FilmStatisticsRepository.get_film_statistics()
        self.assertEqual(stats[0]['year'], 2021)
        self.assertEqual(stats[0]['film_count'], 1)

        self.assertEqual(stats[1]['year'], 2020)
        self.assertEqual(stats[1]['film_count'], 1)


class SessionStatisticsRepositoryTest(TestCase):
    def setUp(self):
        self.session = Session.objects.create(
            dateAndTime=timezone.make_aware(datetime(2023, 1, 1)),
            hallID=Hall.objects.create(numberOfSeats=100),
            filmID=Film.objects.create(name='Film', year=2020,
                                       directorID=Director.objects.create(name='Director', lastName='One', yearOfBirth='1980-01-01')),
            duration=time(2, 30) )

    def test_make_datetime_aware(self):
        self.session.dateAndTime = timezone.make_aware(datetime(2023, 1, 1))
        self.session.save()
        SessionStatisticsRepository.make_datetime_aware()
        self.session.refresh_from_db()
        self.assertTrue(timezone.is_aware(self.session.dateAndTime))



class UserIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_user_registration_and_persistence(self):
        user_data = {
            'name': 'Alice',
            'lastName': 'Smith',
            'yearOfBirth': '1995-06-15',
            'phoneNumber': '0987654321',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }

        response = self.client.post(self.register_url, data=user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(phoneNumber='0987654321').exists())
        user = User.objects.get(phoneNumber='0987654321')
        self.assertEqual(user.name, 'Alice')
        self.assertEqual(user.lastName, 'Smith')
        self.assertEqual(str(user.yearOfBirth), '1995-06-15')

