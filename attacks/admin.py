from django.contrib import admin
from attacks.models import AttackCategory, Attack, AttackCommand



class AttackCommandInline(admin.TabularInline):
    model = AttackCommand


class AttackAdmin(admin.ModelAdmin):
    inlines = [AttackCommandInline]


admin.site.register(AttackCategory)
admin.site.register(Attack, AttackAdmin)
