from django.urls import path
from . import views

urlpatterns = [
    path('ropa/', views.ropa_list, name='ropa_list')
]