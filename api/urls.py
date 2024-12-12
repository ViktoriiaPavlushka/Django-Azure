from django.urls import path
from api import views
from api.views import filmsByYear, filmsByAge
from cinema import views_plotly, views_bokeh, views_interactive

urlpatterns = [
    path('getUser/<int:userID>', views.getUser, name='getUser'),
    path('updateUser/<int:userID>', views.updateUser, name='updateUser'),
    path('deleteUser/<int:userID>', views.deleteUser, name='deleteUser'),
    path('getAllUsers', views.getAllUsers, name='getAllUsers'),


    path('getDirector/<int:directorID>', views.getDirector, name='getDirector'),
    path('addDirector', views.addDirector, name='addDirector'),
    path('updateDirector/<int:directorID>', views.updateDirector, name='updateDirector'),
    path('deleteDirector/<int:directorID>', views.deleteDirector, name='deleteDirector'),
    path('getAllDirectors', views.getAllDirectors, name='getAllDirectors'),


    path('getHall/<int:hallID>', views.getHall, name='getHall'),
    path('addHall', views.addHall, name='addHall'),
    path('updateHall/<int:hallID>', views.updateHall, name='updateHall'),
    path('deleteHall/<int:hallID>', views.deleteHall, name='deleteHall'),
    path('getAllHalls', views.getAllHalls, name='getAllHalls'),


    path('getGenre/<int:genreID>', views.getGenre, name='getGenre'),
    path('addGenre', views.addGenre, name='addGenre'),
    path('updateGenre/<int:genreID>', views.updateGenre, name='updateGenre'),
    path('deleteGenre/<int:genreID>', views.deleteGenre, name='deleteGenre'),
    path('getAllGenres', views.getAllGenres, name='getAllGenres'),


    path('getFilm/<int:filmID>', views.getFilm, name='getFilm'),
    path('addFilm', views.addFilm, name='addFilm'),
    path('updateFilm/<int:filmID>', views.updateFilm, name='updateFilm'),
    path('deleteFilm/<int:filmID>', views.deleteFilm, name='deleteFilm'),
    path('getAllFilms', views.getAllFilms, name='getAllFilms'),


    path('getFilmGenre/<int:filmGenreID>', views.getFilmGenre, name='getFilmGenre'),
    path('addFilmGenre', views.addFilmGenre, name='addFilmGenre'),
    path('updateFilmGenre/<int:filmGenreID>', views.updateFilmGenre, name='updateFilmGenre'),
    path('deleteFilmGenre/<int:filmGenreID>', views.deleteFilmGenre, name='deleteFilmGenre'),
    path('getAllFilmGenres', views.getAllFilmGenres, name='getAllFilmGenres'),


    path('getSeat/<int:seatID>', views.getSeat, name='getSeat'),
    path('addSeat', views.addSeat, name='addSeat'),
    path('updateSeat/<int:seatID>', views.updateSeat, name='updateSeat'),
    path('deleteSeat/<int:seatID>', views.deleteSeat, name='deleteSeat'),
    path('getAllSeats', views.getAllSeats, name='getAllSeats'),


    path('getSession/<int:sessionID>', views.getSession, name='getSession'),
    path('addSession', views.addSession, name='addSession'),
    path('updateSession/<int:sessionID>', views.updateSession, name='updateSession'),
    path('deleteSession/<int:sessionID>', views.deleteSession, name='deleteSession'),
    path('getAllSessions', views.getAllSessions, name='getAllSessions'),


    path('getPrice/<int:priceID>', views.getPrice, name='getPrice'),
    path('addPrice', views.addPrice, name='addPrice'),
    path('updatePrice/<int:priceID>', views.updatePrice, name='updatePrice'),
    path('deletePrice/<int:priceID>', views.deletePrice, name='deletePrice'),
    path('getAllPrices', views.getAllPrices, name='getAllPrices'),


    path('getTicket/<int:ticketID>', views.getTicket, name='getTicket'),
    path('addTicket', views.addTicket, name='addTicket'),
    path('updateTicket/<int:ticketID>', views.updateTicket, name='updateTicket'),
    path('deleteTicket/<int:ticketID>', views.deleteTicket, name='deleteTicket'),
    path('getAllTickets', views.getAllTickets, name='getAllTickets'),

    path('filmsByYear/', filmsByYear, name='filmsByYear'),
    path('filmsByAge/', filmsByAge, name='filmsByAge'),
    path('filmsByGenre/', views.filmsByGenre, name='filmsByGenre'),
    path('dateBySession/', views.dateBySession, name='dateBySession'),
    path('filmsByTicket/', views.filmsByTicket, name='filmsByTicket'),
    path('ticketsByMonth/', views.ticketSales, name='ticketSales'),


    path('dashboardv1/' , views_plotly.graphic1, name='dashboardv1'),
    path('dashboardv2/' , views_bokeh.graphic1 ,  name='dashboardv2'),
    path('interactive_dashboard/' , views_interactive.graphic1 , name='interactive_dashboard'),



]



