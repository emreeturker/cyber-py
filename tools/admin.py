from django.contrib import admin
from tools.models import ToolCategory, Tool, ToolCommand, ToolContentBlock
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin, SortableStackedInline



class ToolCommandInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ToolCommand


class ToolContentBlockInline(SortableStackedInline):
    model = ToolContentBlock
    fk_name = "tool"
    extra = 0


class ToolAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ToolContentBlockInline, ToolCommandInline]


admin.site.register(ToolCategory)
admin.site.register(Tool, ToolAdmin)

