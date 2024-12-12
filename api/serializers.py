from rest_framework import serializers
from cinema.models import User, Film, Ticket, Director, Hall, Price, Genre, FilmGenre, Seat, Session


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class FilmGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmGenre
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    filmID = FilmSerializer(read_only=True)
    hallID = HallSerializer(read_only=True)
    class Meta:
        model = Session
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    userID = UserSerializer(read_only=True)
    seatID = SeatSerializer(read_only=True)
    sessionID = SessionSerializer(read_only=True)
    priceID = PriceSerializer(read_only=True)
    class Meta:
        model = Ticket
        fields = '__all__'


class GenreFilmCountSerializer(serializers.Serializer):
    name = serializers.CharField()  # Назва жанру
    genre_count = serializers.IntegerField()  # Кількість фільмів