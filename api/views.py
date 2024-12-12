from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from cinema.models import User, Film
from api.serializers import (UserSerializer, FilmSerializer, TicketSerializer, DirectorSerializer, HallSerializer,
                             PriceSerializer, GenreSerializer, FilmGenreSerializer, SeatSerializer, SessionSerializer,
                             GenreFilmCountSerializer)
from cinema.singlePointOfAcces import RepositoryManager
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm
from cinema.forms import CreateUserForm, TicketForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError



def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            if User.objects.filter(phoneNumber=form.cleaned_data['phoneNumber']).exists():
                form.add_error('phoneNumber', 'A user with this phone number already exists.')
            form.save()
            return redirect('home')

        else:
            print(form.errors)
    context = {"form": form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        phoneNumber = request.POST.get('phoneNumber')
        password = request.POST.get('password')
        user = authenticate(request, phoneNumber=phoneNumber, password=password)
        if user is not None:
            login(request, user)
            print(f"User {user.phoneNumber}, isAdmin: {user.isAdmin}")  # Додано для перевірки
            if user.isAdmin:
                print("Redirecting to admin home")  # Діагностика
                return redirect('home')  # Прямий шлях
            else:
                print("Redirecting to user home")  # Діагностика
                return redirect('homeUser')  # Прямий шлях
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    context = {}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def homeUser(request):
    return render(request, 'homeUser.html')



@login_required(login_url='login')
def create_ticketUser(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.userID = request.user
            ticket.save()
            return redirect('homeUser')
    else:
        form = TicketForm()
    return render(request, 'create_ticketUser.html', {'form': form})

#User
@api_view(['GET'])
def getUser(request, userID):
    user = RepositoryManager.user.getByID(userID)
    if user:
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateUser(request, userID):
    user = RepositoryManager.user.getByID(userID)
    if user:
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            RepositoryManager.user.update(userID, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteUser(request, userID):
    user = RepositoryManager.user.getByID(userID)
    if user:
        RepositoryManager.user.delete(userID)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllUsers(request):
    users = RepositoryManager.user.getAll()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#Director
@api_view(['GET'])
def getDirector(request, directorID):
    director = RepositoryManager.director.getByID(directorID)
    if director:
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def addDirector(request):
    RepositoryManager.director.add(request.data)
    serializer = DirectorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateDirector(request, directorID):
    director = RepositoryManager.director.getByID(directorID)
    if director:
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            RepositoryManager.director.update(directorID, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteDirector(request, directorID):
    director = RepositoryManager.director.getByID(directorID)
    if director:
        RepositoryManager.director.delete(directorID)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAllDirectors(request):
    directors = RepositoryManager.director.getAll()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#Hall
@api_view(['GET'])
def getHall(request, hallID):
    hall = RepositoryManager.hall.getByID(hallID)
    if hall:
        serializer = HallSerializer(hall)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addHall(request):
    RepositoryManager.hall.add(request.data)
    serializer = HallSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateHall(request, hallID):
    hall = RepositoryManager.hall.getByID(hallID)
    if hall:
        serializer = HallSerializer(hall, data=request.data)
        if serializer.is_valid():
            RepositoryManager.hall.update(hallID, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteHall(request, hallID):
    hall = RepositoryManager.hall.getByID(hallID)
    if hall:
        RepositoryManager.hall.delete(hallID)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllHalls(request):
    halls = RepositoryManager.hall.getAll()
    serializer = HallSerializer(halls, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#Price
@api_view(['GET'])
def getPrice(request, priceID):
    price = RepositoryManager.price.getByID(priceID)
    if price:
        serializer = PriceSerializer(price)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addPrice(request):
    RepositoryManager.price.add(request.data)
    serializer = PriceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updatePrice(request, priceID):
    price = RepositoryManager.price.getByID(priceID)
    if price:
        serializer = PriceSerializer(price, data=request.data)
        if serializer.is_valid():
            RepositoryManager.price.update(priceID, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deletePrice(request, priceID):
    price = RepositoryManager.price.getByID(priceID)
    if price:
        RepositoryManager.price.delete(priceID)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllPrices(request):
    prices = RepositoryManager.price.getAll()
    serializer = PriceSerializer(prices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#Genre
@api_view(['GET'])
def getGenre(request, genreID):
    genre = RepositoryManager.filmGenre.getByID(genreID)
    if genre:
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addGenre(request):
    RepositoryManager.genre.add(request.data)
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateGenre(request, genreID):
    genre = RepositoryManager.genre.getByID(genreID)
    if genre:
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            RepositoryManager.genre.update(genreID, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteGenre(request, genreID):
    genre = RepositoryManager.genre.getByID(genreID)
    if genre:
        RepositoryManager.genre.delete(genreID)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllGenres(request):
    genres = RepositoryManager.genre.getAll()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#Film
@api_view(['GET'])
def getFilm(request, filmID):
    film = RepositoryManager.film.getByID(filmID)
    if film:
        serializer = FilmSerializer(film)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addFilm(request):
    RepositoryManager.film.add(request.data)
    serializer = FilmSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateFilm(request, filmID):
    film = RepositoryManager.film.getByID(filmID)
    if film:
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            RepositoryManager.film.update(filmID, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteFilm(request, filmID):
    film = RepositoryManager.film.getByID(filmID)
    if film:
        RepositoryManager.film.delete(filmID)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllFilms(request):
    films = RepositoryManager.film.getAll()
    serializer = FilmSerializer(films, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#FilmGenre
@api_view(['GET'])
def getFilmGenre(request, filmID, genreID):
    filmGenre = RepositoryManager.filmGenre.getByID(filmID, genreID)
    if filmGenre:
        serializer = FilmGenreSerializer(filmGenre)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addFilmGenre(request):
    RepositoryManager.filmGenre.add(request.data)
    serializer = FilmGenreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateFilmGenre(request, filmID, genreID):
    filmGenre = RepositoryManager.filmGenre.getByID(filmID, genreID)
    if filmGenre:
        serializer = FilmGenreSerializer(filmGenre, data=request.data)
        if serializer.is_valid():
            RepositoryManager.filmGenre.update(filmID, genreID, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteFilmGenre(request, filmID, genreID):
    filmGenre = RepositoryManager.filmGenre.getByID(filmID, genreID)
    if filmGenre:
        RepositoryManager.filmGenre.delete(filmID, genreID)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllFilmGenres(request):
    filmGenres = RepositoryManager.filmGenre.getAll()
    serializer = FilmGenreSerializer(filmGenres, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#Seat
@api_view(['GET'])
def getSeat(request, seatID):
    seat = RepositoryManager.seat.getByID(seatID)
    if seat:
        serializer = SeatSerializer(seat)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addSeat(request):
    RepositoryManager.seat.add(request.data)
    serializer = SeatSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateSeat(request, seatID):
    seat = RepositoryManager.seat.getByID(seatID)
    if seat:
        serializer = SeatSerializer(seat, data=request.data)
        if serializer.is_valid():
            RepositoryManager.seat.update(seatID, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteSeat(request, seatID):
    seat = RepositoryManager.seat.getByID(seatID)
    if seat:
        RepositoryManager.seat.delete(seatID)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllSeats(request):
    seats = RepositoryManager.seat.getAll()
    serializer = SeatSerializer(seats, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#Session
@api_view(['GET'])
def getSession(request, sessionID):
    session = RepositoryManager.session.getByID(sessionID)
    if session:
        serializer = SessionSerializer(session)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addSession(request):
    RepositoryManager.session.add(request.data)
    serializer = SessionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateSession(request, sessionID):
    session = RepositoryManager.session.getByID(sessionID)
    if session:
        serializer = SessionSerializer(session, data=request.data)
        if serializer.is_valid():
            RepositoryManager.session.update(sessionID, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteSession(request, sessionID):
    session = RepositoryManager.session.getByID(sessionID)
    if session:
        RepositoryManager.session.delete(sessionID)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllSessions(request):
    sessions = RepositoryManager.session.getAll()
    serializer = SessionSerializer(sessions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



#Ticket
@api_view(['GET'])
def getTicket(request, ticketID):
    ticket = RepositoryManager.ticket.getByID(ticketID)
    if ticket:
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addTicket(request):
    RepositoryManager.ticket.add(request.data)
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateTicket(request, ticketID):
    ticket = RepositoryManager.ticket.getByID(ticketID)
    if ticket:
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            RepositoryManager.ticket.update(ticketID, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteTicket(request, ticketID):
    ticket = RepositoryManager.ticket.getByID(ticketID)
    if ticket:
        RepositoryManager.ticket.delete(ticketID)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAllTickets(request):
    tickets = RepositoryManager.ticket.getAll()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)





#Statistics
@api_view(['GET'])
def filmsByYear(request):
    data = RepositoryManager.filmStatistics.get_film_statistics()
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def filmsByAge(request):
    data = RepositoryManager.ageStatistics.get_age_statistics()
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def filmsByGenre(request):
    data = RepositoryManager.genreStatistics.get_genre_statistics()
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def dateBySession(request):
    data = RepositoryManager.sessionStatistics.get_session_statistics()
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def filmsByTicket(request):
    data = RepositoryManager.filmTicketStatistics.get_ticket_count_by_film()
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def ticketSales(request):
    data = RepositoryManager.ticketSalesStatistics.get_ticket_sales_for_last_month()
    return Response(data, status=status.HTTP_200_OK)