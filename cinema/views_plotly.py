
import pandas as pd
from django.shortcuts import render
from django_pandas.io import read_frame
import plotly.express as px
from cinema.singlePointOfAcces import RepositoryManager


def graphic1(request):
    filmStatisticsData = RepositoryManager.filmStatistics.get_film_statistics()
    df = read_frame(filmStatisticsData)
    fig = px.bar(df, x='year', y='film_count')
    graph1 = fig.to_html(full_html=False)

    ageStatisticsData = RepositoryManager.ageStatistics.get_age_statistics()
    df = read_frame(ageStatisticsData)
    fig = px.pie(df, values='film_count', names='minAge')
    graph2 = fig.to_html(full_html=False)

    genreStatisticsData = RepositoryManager.genreStatistics.get_genre_statistics()
    df = pd.DataFrame(genreStatisticsData)
    fig = px.pie(df, values='genre', names='films')
    graph3 = fig.to_html(full_html=False)

    sessionStatisticsData = RepositoryManager.sessionStatistics.get_session_statistics()
    df = read_frame(sessionStatisticsData)
    fig = px.line(df, x='dateAndTime', y='ticket_count')
    graph4 = fig.to_html(full_html=False)

    filmTicketStatisticsData = RepositoryManager.filmTicketStatistics.get_ticket_count_by_film()
    df = read_frame(filmTicketStatisticsData)
    fig = px.bar(df, x='name', y='ticket_count')
    graph5 = fig.to_html(full_html=False)

    ticketSalesData = RepositoryManager.ticketSalesStatistics.get_ticket_sales_for_last_month()
    df = read_frame(ticketSalesData)
    fig = px.bar(df, x='name', y='tickets_sold')
    graph6 = fig.to_html(full_html=False)

    return render(request, 'dashboardv1.html', {
        'graph': graph1,
        'graph2': graph2,
        'graph3': graph3,
        'graph4': graph4,
        'graph5': graph5,
        'graph6': graph6})