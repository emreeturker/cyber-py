from django.shortcuts import render, get_object_or_404
from .models import Attack, AttackCategory


def attack_list(request):
    categories = AttackCategory.objects.all()
    return render(request, "attacks/list.html", {"categories":categories})


def attack_detail(request, attack_slug):
    attack = get_object_or_404(Attack, slug=attack_slug)
    commands = attack.commands.order_by("command_category__name")
    return render(request, "attacks/detail.html", {"attack":attack, "commands":commands})














