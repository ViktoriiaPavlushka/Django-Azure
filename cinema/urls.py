from django.urls import path
from django.contrib.auth.decorators import login_required

from api.views import homeUser
from . import views
from .views import (
    DynamicListView, DynamicDetailView,
    DynamicUpdateView, DynamicDeleteView, DynamicCreateView, home, create_ticketAdmin, DynamicListViewUser,
    DynamicDetailViewUser
)
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home, name='home'),
    path('homeUser', homeUser, name='homeUser'),
    path('<str:model_name>/list/', DynamicListView.as_view(), name='list'),
    path('<str:model_name>/listUser/', DynamicListViewUser.as_view(), name='listUser'),
    path('<str:model_name>/<int:pk>/detail/', DynamicDetailView.as_view(), name='detail'),
    path('<str:model_name>/<int:pk>/detailUser/', DynamicDetailViewUser.as_view(), name='detailUser'),
    path('<str:model_name>/create/', DynamicCreateView.as_view(), name='create'),
    path('<str:model_name>/<int:pk>/update/', DynamicUpdateView.as_view(), name='update'),
    path('<str:model_name>/<int:pk>/delete/', DynamicDeleteView.as_view(), name='delete'),

    path('create_ticketAdmin/', views.create_ticketAdmin, name='create_ticketAdmin'),






]