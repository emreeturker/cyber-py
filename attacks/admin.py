from django.contrib import admin
from attacks.models import AttackCategory, Attack, AttackCommandElement
from adminsortable2.admin import SortableAdminBase, SortableStackedInline


class AttackCommandElementInline(SortableStackedInline):
    model = AttackCommandElement
    fk_name = "attack"
    extra = 0
    fields = ("order", "text", "block_description", "command_text", "command_description", "command_category", "image")


class AttackAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [AttackCommandElementInline]


admin.site.register(AttackCategory)
admin.site.register(Attack, AttackAdmin)