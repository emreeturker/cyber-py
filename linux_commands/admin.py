from django.contrib import admin
from linux_commands.models import LinuxCommandCategory, LinuxCommand, LinuxCommandContentBlock
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin, SortableStackedInline



class LinuxCommandInline(SortableInlineAdminMixin, admin.TabularInline):
    model = LinuxCommand


class LinuxCommandContentBlockInline(SortableStackedInline):
    model = LinuxCommandContentBlock
    extra = 0


class LinuxCommandCategoryAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [LinuxCommandInline, LinuxCommandContentBlockInline]


admin.site.register(LinuxCommandCategory, LinuxCommandCategoryAdmin)




