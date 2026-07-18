from django.urls import path 
from . import views 


app_name = 'attacks'


urlpatterns = [
    path("", views.attack_list, name="list"),
    path("<slug:attack_slug>/", views.attack_detail, name="detail"),
]