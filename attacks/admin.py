import nested_admin
from django.contrib import admin
from attacks.models import AttackCategory, Attack, AttackCommandElement, AttackCommandElementImage


class AttackCommandElementImageInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = AttackCommandElementImage
    fk_name = "element"
    extra = 0
    fields = ("order", "image")
    sortable_field_name = "order"


class AttackCommandElementInline(nested_admin.SortableHiddenMixin, nested_admin.NestedStackedInline):
    model = AttackCommandElement
    fk_name = "attack"
    extra = 0
    fields = ("order", "text", "block_description", "command_text", "command_description", "command_category")
    sortable_field_name = "order"
    inlines = [AttackCommandElementImageInline]


class AttackAdmin(nested_admin.NestedModelAdmin):
    inlines = [AttackCommandElementInline]


admin.site.register(AttackCategory)
admin.site.register(Attack, AttackAdmin)