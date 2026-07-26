from django.contrib import admin
from tools.models import ToolCategory, Tool, ToolCommand
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin



class ToolCommandInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ToolCommand


class ToolAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ToolCommandInline]


admin.site.register(ToolCategory)
admin.site.register(Tool, ToolAdmin)

