from cinema.repositories import (UserRepository, FilmRepository, FilmGenreRepository, SeatRepository,
                                 SessionRepository, TicketRepository, HallRepository, PriceRepository,
                                 DirectorRepository, GenreRepository, FilmStatisticsRepository, AgeStatisticsRepository,
                                 GenreStatisticsRepository, SessionStatisticsRepository, FilmTicketStatisticsRepository,
                                 TicketSalesRepository)

class RepositoryManager:
    user = UserRepository
    film = FilmRepository
    filmGenre = FilmGenreRepository
    genre = GenreRepository
    seat = SeatRepository
    session = SessionRepository
    ticket = TicketRepository
    hall = HallRepository
    price = PriceRepository
    director = DirectorRepository
    filmStatistics = FilmStatisticsRepository
    ageStatistics = AgeStatisticsRepository
    genreStatistics = GenreStatisticsRepository
    sessionStatistics = SessionStatisticsRepository
    filmTicketStatistics = FilmTicketStatisticsRepository
    ticketSalesStatistics = TicketSalesRepository
