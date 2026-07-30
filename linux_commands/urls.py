from django.urls import path 
from . import views 

app_name = 'linux_commands'


urlpatterns = [
    path("", views.linux_list, name="list"),
]