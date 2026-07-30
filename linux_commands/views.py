from django.shortcuts import render
from .models import LinuxCommandCategory



def linux_list(request):
    categories = LinuxCommandCategory.objects.all()
    return render(request, "linux_commands/list.html", {"categories": categories})