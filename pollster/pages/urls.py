from django.urls import path
from . import views

urlpatterns = [
    # by leaving path empty, that means it will just be /polls
    path('', views.index, name='index'),
]