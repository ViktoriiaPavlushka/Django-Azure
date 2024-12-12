# repositories.py
from django.db.models import Count
from .models import User, Director, Hall, Price, Genre, Film, FilmGenre, Seat, Session, Ticket
from datetime import datetime, timedelta
import calendar
from django.utils import timezone

class UserRepository:
    @staticmethod
    def add(userData):
        user = User(**userData)
        user.save()

    @staticmethod
    def getByPhoneNumber(phoneNumber):
        return User.objects.filter(phoneNumber=phoneNumber).first()

    @staticmethod
    def getByID(userID):
        return User.objects.filter(userID=userID).first()

    @staticmethod
    def getAll():
        return list(User.objects.all())

    @staticmethod
    def delete(userID):
        User.objects.filter(userID=userID).delete()

    @staticmethod
    def update(userID, userData):
        user = User.objects.filter(userID=userID).first()
        if user:
            for key, value in userData.items():
                setattr(user, key, value)
            user.save()


class DirectorRepository:
    @staticmethod
    def add(directorData):
        director = Director(**directorData)
        director.save()

    @staticmethod
    def getByID(directorID):
        return Director.objects.filter(directorID=directorID).first()

    @staticmethod
    def getAll():
        return list(Director.objects.all())

    @staticmethod
    def delete(directorID):
        Director.objects.filter(directorID=directorID).delete()

    @staticmethod
    def update(directorID, directorData):
        director = Director.objects.filter(directorID=directorID).first()
        if director:
            for key, value in directorData.items():
                setattr(director, key, value)
            director.save()


class HallRepository:
    @staticmethod
    def add(hallData):
        hall = Hall(**hallData)
        hall.save()

    @staticmethod
    def getByID(hallID):
        return Hall.objects.filter(hallID=hallID).first()

    @staticmethod
    def getAll():
        return list(Hall.objects.all())

    @staticmethod
    def delete(hallID):
        Hall.objects.filter(hallID=hallID).delete()

    @staticmethod
    def update(hallID, hallData):
        hall = Hall.objects.filter(hallID=hallID).first()
        if hall:
            for key, value in hallData.items():
                setattr(hall, key, value)
            hall.save()


class PriceRepository:
    @staticmethod
    def add(priceData):
        price = Price(**priceData)
        price.save()

    @staticmethod
    def getByID(priceID):
        return Price.objects.filter(priceID=priceID).first()

    @staticmethod
    def getAll():
        return list(Price.objects.all())

    @staticmethod
    def delete(priceID):
        Price.objects.filter(priceID=priceID).delete()

    @staticmethod
    def update(priceID, priceData):
        price = Price.objects.filter(priceID=priceID).first()
        if price:
            for key, value in priceData.items():
                setattr(price, key, value)
            price.save()


class GenreRepository:
    @staticmethod
    def add(genreData):
        genre = Genre(**genreData)
        genre.save()

    @staticmethod
    def getByID(genreID):
        return Genre.objects.filter(genreID=genreID).first()

    @staticmethod
    def getAll():
        return list(Genre.objects.all())

    @staticmethod
    def delete(genreID):
        Genre.objects.filter(genreID=genreID).delete()

    @staticmethod
    def update(genreID, genreData):
        genre = Genre.objects.filter(genreID=genreID).first()
        if genre:
            for key, value in genreData.items():
                setattr(genre, key, value)
            genre.save()


class FilmRepository:
    @staticmethod
    def add(filmData):
        film = Film(**filmData)
        film.save()

    @staticmethod
    def getByID(filmID):
        return Film.objects.filter(filmID=filmID).first()

    @staticmethod
    def getAll():
        return list(Film.objects.all())

    @staticmethod
    def delete(filmID):
        Film.objects.filter(filmID=filmID).delete()

    @staticmethod
    def update(filmID, filmData):
        film = Film.objects.filter(filmID=filmID).first()
        if film:
            for key, value in filmData.items():
                setattr(film, key, value)
            film.save()


class FilmGenreRepository:
    @staticmethod
    def add(filmGenreData):
        film_genre = FilmGenre(**filmGenreData)
        film_genre.save()

    @staticmethod
    def getByID(filmID, genreID):
        return FilmGenre.objects.filter(film_id=filmID, genre_id=genreID).first()

    @staticmethod
    def getAll():
        return list(FilmGenre.objects.all())

    @staticmethod
    def delete(filmID, genreID):
        FilmGenre.objects.filter(film_id=filmID, genre_id=genreID).delete()

    @staticmethod
    def update(filmID, genreID, filmGenreData):
        film_genre = FilmGenre.objects.filter(ffilm_id=filmID, genre_id=genreID).first()
        if film_genre:
            for key, value in filmGenreData.items():
                setattr(film_genre, key, value)
            film_genre.save()


class SeatRepository:
    @staticmethod
    def add(seatData):
        seat = Seat(**seatData)
        seat.save()

    @staticmethod
    def getByID(seatID):
        return Seat.objects.filter(seatID=seatID).first()

    @staticmethod
    def getAll():
        return list(Seat.objects.all())

    @staticmethod
    def delete(seatID):
        Seat.objects.filter(seatID=seatID).delete()

    @staticmethod
    def update(seatID, seatData):
        seat = Seat.objects.filter(seatID=seatID).first()
        if seat:
            for key, value in seatData.items():
                setattr(seat, key, value)
            seat.save()


class SessionRepository:
    @staticmethod
    def add(sessionData):
        session = Session(**sessionData)
        session.save()

    @staticmethod
    def getByID(sessionID):
        return Session.objects.filter(sessionID=sessionID).first()

    @staticmethod
    def getAll():
        return list(Session.objects.all())

    @staticmethod
    def delete(sessionID):
        Session.objects.filter(sessionID=sessionID).delete()

    @staticmethod
    def update(sessionID, sessionData):
        session = Session.objects.filter(sessionID=sessionID).first()
        if session:
            for key, value in sessionData.items():
                setattr(session, key, value)
            session.save()


class TicketRepository:
    @staticmethod
    def add(ticketData):
        ticket = Ticket(**ticketData)
        ticket.save()

    @staticmethod
    def getByID(ticketID):
        return Ticket.objects.filter(ticketID=ticketID).first()

    @staticmethod
    def getAll():
        return list(Ticket.objects.all())

    @staticmethod
    def delete(ticketID):
        Ticket.objects.filter(ticketID=ticketID).delete()

    @staticmethod
    def update(ticketID, ticketData):
        ticket = Ticket.objects.filter(ticketID=ticketID).first()
        if ticket:
            for key, value in ticketData.items():
                setattr(ticket, key, value)
            ticket.save()






#кількість фільмів в кожному році
class FilmStatisticsRepository:
    @staticmethod
    def get_film_statistics():
        return Film.objects.values('year').annotate(film_count=Count('filmID')).order_by('-year')

class AgeStatisticsRepository:
    @staticmethod
    def get_age_statistics():
        return Film.objects.values('minAge').annotate(film_count=Count('filmID')).order_by('-minAge')

class GenreStatisticsRepository:
    @staticmethod
    def get_genre_statistics():
        genres = Genre.objects.prefetch_related('film_set').all()
        result = []
        for genre in genres:
            films = genre.film_set.all()
            result.append({
                'genre': genre.name,
                'films': [film.name for film in films]
            })
        return result

class SessionStatisticsRepository:
    @staticmethod
    def get_session_statistics():
        return (
            Session.objects.annotate(ticket_count=Count('ticket'))
            .values('dateAndTime', 'ticket_count')
            .order_by('-dateAndTime')
        )

    @staticmethod
    def make_datetime_aware():
        sessions = Session.objects.all()
        for session in sessions:
            if timezone.is_naive(session.dateAndTime):
                session.dateAndTime = timezone.make_aware(session.dateAndTime)
                session.save()

class FilmTicketStatisticsRepository:
    @staticmethod
    def get_ticket_count_by_film():
        return (
            Film.objects.annotate(ticket_count=Count('session__ticket'))
            .values('name', 'ticket_count')
            .order_by('-ticket_count')
        )

class TicketSalesRepository:
    @staticmethod
    def get_ticket_sales_for_last_month():
        today = datetime.today()
        first_day_of_last_month = today.replace(day=1) - timedelta(days=1)
        first_day_of_last_month = first_day_of_last_month.replace(day=1)
        last_day_of_last_month = today.replace(day=1) - timedelta(days=1)
        films_with_sales = (
            Film.objects
            .filter(session__dateAndTime__range=[first_day_of_last_month,
                                                 last_day_of_last_month])
            .annotate(tickets_sold=Count('session__ticket'))
            .values('name', 'tickets_sold')
            .order_by('-tickets_sold')
        )

        return films_with_sales