from django import forms
from django.contrib import admin
from ports.models import PortCategory, Port, PortContentBlock
from adminsortable2.admin import SortableAdminBase, SortableStackedInline



class PortInlineForm(forms.ModelForm):
    class Meta:
        model = Port
        fields = "__all__"
        widgets = {
            "vulnerability": forms.Textarea(attrs={"rows": 2, "cols": 40}),
        }


class PortInline(admin.TabularInline):
    model = Port
    form = PortInlineForm


class PortContentBlockInline(SortableStackedInline):
    model = PortContentBlock
    extra = 0


class PortCategoryAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PortInline, PortContentBlockInline]


admin.site.register(PortCategory, PortCategoryAdmin)
