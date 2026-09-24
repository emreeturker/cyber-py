from django.shortcuts import render
from .models import LinuxCommandCategory



def linux_list(request):
    categories = LinuxCommandCategory.objects.prefetch_related("commands", "content_blocks__related_attack", "content_blocks__related_tool")
    return render(request, "linux_commands/list.html", {"categories": categories})