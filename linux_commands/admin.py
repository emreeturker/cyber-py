import nested_admin
from django.contrib import admin
from linux_commands.models import LinuxCommandCategory, LinuxCommandElement, LinuxCommandElementImage


class LinuxCommandElementImageInline(nested_admin.SortableHiddenMixin, nested_admin.NestedTabularInline):
    model = LinuxCommandElementImage
    fk_name = "element"
    extra = 0
    fields = ("order", "image")
    sortable_field_name = "order"


class LinuxCommandElementInline(nested_admin.SortableHiddenMixin, nested_admin.NestedStackedInline):
    model = LinuxCommandElement
    fk_name = "category"
    extra = 0
    fields = ("order", "text", "block_description", "command_text", "command_description", "command_category")
    sortable_field_name = "order"
    inlines = [LinuxCommandElementImageInline]


class LinuxCommandCategoryAdmin(nested_admin.NestedModelAdmin):
    inlines = [LinuxCommandElementInline]


admin.site.register(LinuxCommandCategory, LinuxCommandCategoryAdmin)