from django.contrib import admin
from tools.models import ToolCategory, Tool, ToolCommandElement
from adminsortable2.admin import SortableAdminBase, SortableStackedInline


class ToolCommandElementInline(SortableStackedInline):
    model = ToolCommandElement
    fk_name = "tool"
    extra = 0
    fields = ("order", "text", "block_description", "command_text", "command_description", "command_category", "image")


class ToolAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ToolCommandElementInline]


admin.site.register(ToolCategory)
admin.site.register(Tool, ToolAdmin)