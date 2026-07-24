from django.shortcuts import render
from attacks.models import Attack
from tools.models import Tool
from itertools import chain 


def home(request):
    recent_attacks = Attack.objects.all().order_by('-created_at')[:1]
    recent_tools = Tool.objects.all().order_by('-created_at')[:1]
    combined = chain(recent_attacks, recent_tools)
    recent_items = sorted(combined, key=lambda x: x.created_at, reverse=True )
    return render (request, "home.html", {'recent_items':recent_items})



