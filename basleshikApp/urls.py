from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group', views.group, name='group'),
    path('emin/<int:id>/', views.emin, name='emin'),
    path('competitions', views.competitions, name='competitions'),
]
