from django.contrib import admin
from tools.models import ToolCategory, Tool, ToolCommand



class ToolCommandInline(admin.TabularInline):
    model = ToolCommand


class ToolAdmin(admin.ModelAdmin):
    inlines = [ToolCommandInline]


admin.site.register(ToolCategory)
admin.site.register(Tool, ToolAdmin)

