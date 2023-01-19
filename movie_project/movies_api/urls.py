from django.urls import path,include
from . import views

urlpatterns=[path('',views.movies_api),
            path('<int:id>',views.get_more_movies)]