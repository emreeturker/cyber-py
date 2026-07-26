from django.contrib import admin
from attacks.models import AttackCategory, Attack, AttackCommand
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin



class AttackCommandInline(SortableInlineAdminMixin, admin.TabularInline):
    model = AttackCommand


class AttackAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [AttackCommandInline]


admin.site.register(AttackCategory)
admin.site.register(Attack, AttackAdmin)
