from django.urls import path,include
from . import views

urlpatterns=[path('',views.show_count),
            path('reset/',views.reset_count,name='reset')]
