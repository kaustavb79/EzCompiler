from django.urls import path
from app_home import views

app_name = 'app_home'

urlpatterns = [
    path('' , views.home , name="index")    
]