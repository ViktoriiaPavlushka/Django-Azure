from django import forms
from django.forms import ModelForm
from .models import User, Director, Hall, Price, Genre, Film, Seat, Session, Ticket
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class HallForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = 'name', 'directorID', 'year', 'description', 'country', 'minAge'

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = '__all__'

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = '__all__'


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['sessionID', 'priceID', 'seatID']


class TicketFormAdmin(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['sessionID', 'priceID', 'seatID']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['phoneNumber', 'name', 'lastName', 'yearOfBirth', 'password']
