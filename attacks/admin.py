from django.contrib import admin
from attacks.models import AttackCategory, Attack, AttackCommand, AttackCommandCategory
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin



class AttackCommandInline(SortableInlineAdminMixin, admin.TabularInline):
    model = AttackCommand


class AttackCommandCategoryInline(admin.StackedInline):
    model = AttackCommandCategory
    fk_name = "attack"
    extra = 0


class AttackAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [AttackCommandCategoryInline, AttackCommandInline]


admin.site.register(AttackCategory)
admin.site.register(Attack, AttackAdmin)
