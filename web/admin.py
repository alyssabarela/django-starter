from django.contrib import admin
from .models import Placeholder


class PlaceholderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['placeholder']}),
    ]
    inlines = []
    list_display = ('placeholder',)
    list_filter = ['placeholder']
    search_fields = ['placeholder']


admin.site.register(Placeholder, PlaceholderAdmin)
