from django.urls import path
from . import views

app_name = 'gpio'
urlpatterns = [
    path('', views.home, name='home'),
    path('api/', views.home, name='home_api'),
    path('token/', views.get_csrf, name='token'),   
]