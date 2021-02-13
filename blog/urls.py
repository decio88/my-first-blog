from django.urls import path
from . import views

urlpatterns = [
    path('', views.post__list, name='post_list'),
]
