import nested_admin
from django.contrib import admin
from tools.models import ToolCategory, Tool, ToolCommandElement, ToolCommandElementImage


class ToolCommandElementImageInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = ToolCommandElementImage
    fk_name = "element"
    extra = 0
    fields = ("order", "image")
    sortable_field_name = "order"


class ToolCommandElementInline(nested_admin.SortableHiddenMixin, nested_admin.NestedStackedInline):
    model = ToolCommandElement
    fk_name = "tool"
    extra = 0
    fields = ("order", "text", "block_description", "command_text", "command_description", "command_category")
    sortable_field_name = "order"
    inlines = [ToolCommandElementImageInline]


class ToolAdmin(nested_admin.NestedModelAdmin):
    inlines = [ToolCommandElementInline]


admin.site.register(ToolCategory)
admin.site.register(Tool, ToolAdmin)