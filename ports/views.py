from django.shortcuts import render
from .models import PortCategory



def port_list(request):
    categories = PortCategory.objects.prefetch_related("ports", "content_blocks__related_attack", "content_blocks__related_tool")
    return render(request, "ports/list.html", {"categories": categories})

