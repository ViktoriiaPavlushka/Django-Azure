from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.palettes import Category20c
from bokeh.models import ColumnDataSource
from cinema.singlePointOfAcces import RepositoryManager
from bokeh.transform import cumsum
import pandas as pd
import numpy as np


def graphic1(request):
    # Graph 1: Number of films per year
    film_statistics = RepositoryManager.filmStatistics.get_film_statistics()
    if not film_statistics.exists():
        print("No data available for films by year")
        df1 = pd.DataFrame({'year': [], 'film_count': []})
    else:
        df1 = pd.DataFrame(film_statistics).drop_duplicates(subset=['year'])
    source1 = ColumnDataSource(data=dict(
        year=list(map(str, df1['year'])),  # Роки як рядки
        film_count=df1['film_count']
    ))
    p1 = figure(
        x_axis_label='Year',
        y_axis_label='Film Count',
        title='Number of Films by Year',
        x_range=list(map(str, df1['year']))
    )
    p1.vbar(x='year', top='film_count', width=0.9, source=source1)
    p1.xaxis.major_label_orientation = 1.2  # Кут нахилу підписів на осі X
    p1.xgrid.grid_line_color = None
    p1.ygrid.grid_line_dash = [6, 4]

    # Graph 2: Number of films per age
    age_statistics = RepositoryManager.ageStatistics.get_age_statistics()
    if not age_statistics.exists():
        print("No data available for films by age restrictions")
        df2 = pd.DataFrame({'minAge': [], 'film_count': []})
    else:
        df2 = pd.DataFrame(age_statistics).drop_duplicates(subset=['minAge'])
    df2['angle'] = df2['film_count'] / df2['film_count'].sum() * 2 * np.pi  # Кути секторів
    df2['color'] = Category20c[len(df2)] if len(df2) <= 20 else Category20c[20]  # Кольори секторів
    source2 = ColumnDataSource(df2)
    p2 = figure(
        height=400,
        title="Film Count by Age Restriction",
        toolbar_location=None,
        tools="hover",
        tooltips="@minAge: @film_count",
        x_range=(-0.5, 1.0),
    )
    p2.wedge(
        x=0,
        y=1,
        radius=0.4,
        start_angle=cumsum('angle', include_zero=True),
        end_angle=cumsum('angle'),
        line_color="white",
        fill_color='color',
        legend_field='minAge',
        source=source2,
    )
    p2.axis.axis_label = None
    p2.axis.visible = False
    p2.grid.grid_line_color = None
    script, div = components(p2)

    # Graph 3: Number of tickets per session
    session_statistics = RepositoryManager.sessionStatistics.get_session_statistics()
    if not session_statistics.exists():
        print("No data available for sessions")
        df4 = pd.DataFrame({'dateAndTime': [], 'ticket_count': []})
    else:
        RepositoryManager.sessionStatistics.make_datetime_aware()  # Ensure datetime awareness
        df4 = pd.DataFrame(session_statistics)
        df4['dateAndTime'] = pd.to_datetime(df4['dateAndTime'])
    source4 = ColumnDataSource(df4)
    p4 = figure(x_axis_type='datetime', x_axis_label='Date and Time', y_axis_label='Ticket Count', title='Tickets sold per session')
    p4.line(x='dateAndTime', y='ticket_count', source=source4)

    # Graph 4: Number of tickets per film
    film_ticket_statistics = RepositoryManager.filmTicketStatistics.get_ticket_count_by_film()
    if not film_ticket_statistics.exists():
        print("No data available for tickets by film")
        df5 = pd.DataFrame({'name': [], 'ticket_count': []})
    else:
        df5 = pd.DataFrame(film_ticket_statistics).drop_duplicates(subset=['name'])
    source5 = ColumnDataSource(df5)
    p5 = figure(x_axis_label='Film', y_axis_label='Ticket Count', title='Tickets sold per film', x_range=df5['name'])
    p5.vbar(x='name', top='ticket_count', width=0.9, source=source5)

    # Graph 5: Tickets sold last month
    ticket_sales = RepositoryManager.ticketSalesStatistics.get_ticket_sales_for_last_month()
    if not ticket_sales.exists():
        print("No data available for ticket sales")
        df6 = pd.DataFrame({'name': [], 'tickets_sold': []})
    else:
        df6 = pd.DataFrame(ticket_sales).drop_duplicates(subset=['name'])
    source6 = ColumnDataSource(df6)
    p6 = figure(x_axis_label='Film', y_axis_label='Tickets Sold', title='Tickets sold last month', x_range=df6['name'])
    p6.vbar(x='name', top='tickets_sold', width=0.9, source=source6)

    # Combine layouts
    script1, div1 = components(p1)
    script2, div2 = components(p2)
    script3, div3 = components(p4)
    script4, div4 = components(p5)
    script5, div5 = components(p6)

    return render(request, 'dashboardv2.html', {
        'script': script1 + script2 + script3 + script4 + script5,
        'div1': div1,
        'div2': div2,
        'div3': div3,
        'div4': div4,
        'div5': div5
    })