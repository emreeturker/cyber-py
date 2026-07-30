from django.contrib import admin
from linux_commands.models import LinuxCommandCategory, LinuxCommand
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin



class LinuxCommandInline(SortableInlineAdminMixin, admin.TabularInline):
    model = LinuxCommand


class LinuxCommandCategoryAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [LinuxCommandInline]


admin.site.register(LinuxCommandCategory, LinuxCommandCategoryAdmin)




