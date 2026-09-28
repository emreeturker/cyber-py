from django.shortcuts import render
from .models import LinuxCommandCategory


def linux_list(request):
    categories = LinuxCommandCategory.objects.prefetch_related("elements__command_category", "elements__images")
    return render(request, "linux_commands/list.html", {"categories": categories})