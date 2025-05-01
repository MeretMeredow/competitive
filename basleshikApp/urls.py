from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group', views.group, name='group'),
    path('emin', views.emin, name='emin'),
]
