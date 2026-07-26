from django.shortcuts import render, get_object_or_404
from .models import Tool, ToolCategory


def tool_list(request):
    categories = ToolCategory.objects.all()
    return render(request, "tools/list.html", {"categories":categories})


def tool_detail(request, tool_slug):
    tool = get_object_or_404(Tool, slug=tool_slug)
    commands = tool.commands.all()
    return render(request, "tools/detail.html", {"tool":tool, "commands":commands})



