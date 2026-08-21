from django.urls import path
from . import views

app_name = 'ports'


urlpatterns = [
    path("", views.port_list, name="list"),
]