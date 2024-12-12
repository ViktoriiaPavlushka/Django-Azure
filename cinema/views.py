from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import *
from django.contrib import messages
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import FormView
from django.shortcuts import render, redirect
from .forms import TicketForm

MODEL_MAP = {
    "film": Film,
    "director": Director,
    "genre": Genre,
    "hall": Hall,
    "seat": Seat,
    "price" : Price,
    "session": Session,
}

FORM_MAP = {
    "film": FilmForm,
    "director": DirectorForm,
    "genre": GenreForm,
    "hall": HallForm,
    "seat": SeatForm,
    "price" : PriceForm,
    "session": SessionForm,
}

def home(request):
    return render(request, 'home.html')

class DynamicListView(ListView):
    template_name = "list.html"

    def get_queryset(self):
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP.get(model_name.lower())
        if not model:
            raise ValueError(f"Model '{model_name}' not found.")
        return model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP[model_name.lower()]
        context["model_name"] = model_name.capitalize()
        context["field_names"] = [field.name for field in model._meta.fields]
        context["items"] = self.object_list
        return context


class DynamicListViewUser(ListView):
    template_name = "listUser.html"

    def get_queryset(self):
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP.get(model_name.lower())
        if not model:
            raise ValueError(f"Model '{model_name}' not found.")
        return model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP[model_name.lower()]
        context["model_name"] = model_name.capitalize()
        context["field_names"] = [field.name for field in model._meta.fields]
        context["items"] = self.object_list
        return context



class DynamicDetailView(DetailView):
    template_name = "detail.html"

    def get_object(self):
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP.get(model_name.lower())
        if not model:
            raise ValueError(f"Model '{model_name}' not found.")
        return get_object_or_404(model, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP[model_name.lower()]
        context["model_name"] = model_name.capitalize()
        context["field_names"] = [field.name for field in model._meta.fields]
        context["item"] = self.object
        return context


class DynamicDetailViewUser(DetailView):
    template_name = "detailUser.html"

    def get_object(self):
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP.get(model_name.lower())
        if not model:
            raise ValueError(f"Model '{model_name}' not found.")
        return get_object_or_404(model, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP[model_name.lower()]
        context["model_name"] = model_name.capitalize()
        context["field_names"] = [field.name for field in model._meta.fields]
        context["item"] = self.object
        return context



class DynamicCreateView(CreateView):
    template_name = "form.html"

    def get_form_class(self):
        model_name = self.kwargs.get("model_name")
        form_class = FORM_MAP.get(model_name.lower())
        if not form_class:
            raise ValueError(f"Form for model '{model_name}' not found.")
        return form_class

    def form_valid(self, form):
        # Save the object and get the instance
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        context["model_name"] = model_name.capitalize()
        context["form_title"] = f"Add New {model_name.capitalize()}"
        return context

    def get_success_url(self):
        model_name = self.kwargs.get("model_name")
        # Redirect to the detail page of the newly created object
        return reverse_lazy("detail", kwargs={"model_name": model_name.lower(), "pk": self.object.pk})



class DynamicUpdateView(UpdateView):
    template_name = "form.html"

    def get_form_class(self):
        model_name = self.kwargs.get("model_name")
        form_class = FORM_MAP.get(model_name.lower())
        if not form_class:
            raise ValueError(f"Form for model '{model_name}' not found.")
        return form_class

    def get_object(self):
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP.get(model_name.lower())
        if not model:
            raise ValueError(f"Model '{model_name}' not found.")
        return get_object_or_404(model, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        context["model_name"] = model_name.capitalize()
        context["form_title"] = f"Edit {model_name.capitalize()}"
        return context

    def get_success_url(self):
        model_name = self.kwargs.get("model_name")
        return reverse_lazy("list", kwargs={"model_name": model_name.lower()})


class DynamicDeleteView(DeleteView):
    template_name = "delete.html"

    def get_object(self):
        model_name = self.kwargs.get("model_name")
        model = MODEL_MAP.get(model_name.lower())
        if not model:
            raise ValueError(f"Model '{model_name}' not found.")
        return get_object_or_404(model, pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.kwargs.get("model_name")
        context["model_name"] = model_name.capitalize()
        return context

    def get_success_url(self):
        model_name = self.kwargs.get("model_name")
        return reverse_lazy("list", kwargs={"model_name": model_name.lower()})


def create_ticketAdmin(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        try:
            user = User.objects.get(phoneNumber=phone)
        except User.DoesNotExist:
            messages.error(request, "User with this phone number does not exist.")
            return redirect('create_ticketAdmin')

        form = TicketFormAdmin(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.userID = user
            ticket.save()
            messages.success(request, "Ticket created successfully!")
            return redirect('home')
    else:
        form = TicketFormAdmin()
    return render(request, 'create_ticket.html', {'form': form})


#
# def create_ticketAdmin(request):
#     if request.method == 'POST':
#         phone = request.POST.get('phone')
#         try:
#             user = User.objects.get(phoneNumber=phone)
#         except User.DoesNotExist:
#             messages.error(request, "User with this phone number does not exist.")
#             return redirect('create_ticketAdmin')
#
#         # Отримуємо сеанс
#         sessionID = request.POST.get('sessionID')
#         try:
#             session = Session.objects.get(sessionID=sessionID)
#         except Session.DoesNotExist:
#             messages.error(request, "Session does not exist.")
#             return redirect('create_ticketAdmin')
#
#         # Створюємо форму з переданим session
#         form = TicketFormAdmin(request.POST, session=session)
#
#         if form.is_valid():
#             seatID = form.cleaned_data['seatID']
#             seat = Seat.objects.get(seatID=seatID)
#
#             # Перевірка, чи місце ще вільне
#             if Ticket.objects.filter(seatID=seat, sessionID=session).exists():
#                 messages.error(request, "This seat is already booked.")
#                 return redirect('create_ticketAdmin')
#
#             ticket = form.save(commit=False)
#             ticket.userID = user
#             ticket.sessionID = session
#             ticket.save()
#
#             messages.success(request, "Ticket created successfully!")
#             return redirect('home')
#     else:
#         # Отримуємо всі сеанси для відображення в шаблоні
#         sessions = Session.objects.all()
#         form = TicketFormAdmin()
#
#     return render(request, 'create_ticket.html', {
#         'form': form,
#         'sessions': sessions,  # Додаємо доступні сеанси
#     })

