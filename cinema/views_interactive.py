from datetime import datetime

import plotly
from django.shortcuts import render
from .models import Film
from .repositories import FilmRepository, TicketRepository, UserRepository
import plotly.graph_objs as go
import json


def graphic1(request):
    # Get all films for the dropdown
    films = FilmRepository.getAll()

    selected_films = []
    if request.method == "POST":
        selected_film_ids = request.POST.getlist('films')  # Get selected films
        selected_film_ids = [int(film_id) for film_id in selected_film_ids if film_id.isdigit()]  # Ensure valid IDs

        if selected_film_ids:
            selected_films = Film.objects.filter(filmID__in=selected_film_ids)

        # Generate age statistics
        age_groups = {}  # Dictionary to store age ranges and counts
        for film in selected_films:
            tickets = [ticket for ticket in TicketRepository.getAll() if ticket.sessionID.filmID == film]
            for ticket in tickets:
                user = UserRepository.getByID(ticket.userID.userID)
                if user:
                    age = (datetime.now().date() - user.yearOfBirth).days // 365  # Calculate age
                    age_range = f"{(age // 5) * 5}-{((age // 5) * 5) + 4}"  # Define age range (e.g., 20-24, 25-29)
                    if age_range in age_groups:
                        age_groups[age_range] += 1
                    else:
                        age_groups[age_range] = 1

        # Prepare data for the pie chart
        labels = list(age_groups.keys())
        values = list(age_groups.values())

        # Create pie chart using Plotly
        fig = go.Figure(
            data=[go.Pie(labels=labels, values=values, hole=0.3)]  # `hole=0.3` makes it a donut chart
        )

        fig.update_layout(
            title="Age Distribution of Buyers",
        )

        # Convert plotly figure to JSON
        plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

        return render(request, 'interactive_dashboard.html', {'films': films, 'plot_json': plot_json})

    return render(request, 'interactive_dashboard.html', {'films': films})
