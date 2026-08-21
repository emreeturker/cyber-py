from django import forms
from django.contrib import admin
from ports.models import PortCategory, Port



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


class PortCategoryAdmin(admin.ModelAdmin):
    inlines = [PortInline]


admin.site.register(PortCategory, PortCategoryAdmin)
