from django.shortcuts import render
from .models import PortCategory



def port_list(request):
    categories = PortCategory.objects.all()
    return render(request, "ports/list.html", {"categories": categories})

