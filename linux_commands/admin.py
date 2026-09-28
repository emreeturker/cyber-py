from django.contrib import admin
from linux_commands.models import LinuxCommandCategory, LinuxCommandElement
from adminsortable2.admin import SortableAdminBase, SortableStackedInline


class LinuxCommandElementInline(SortableStackedInline):
    model = LinuxCommandElement
    fk_name = "category"
    extra = 0
    fields = ("order", "text", "block_description", "command_text", "command_description", "command_category", "image")


class LinuxCommandCategoryAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [LinuxCommandElementInline]


admin.site.register(LinuxCommandCategory, LinuxCommandCategoryAdmin)