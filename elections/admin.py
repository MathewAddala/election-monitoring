from django.contrib import admin
from .models import Election, ElectionUpdate


class ElectionUpdateInline(admin.TabularInline):
    model = ElectionUpdate
    extra = 1


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display  = ['title', 'location', 'election_date', 'status']
    list_filter   = ['status']
    search_fields = ['title', 'location']
    inlines       = [ElectionUpdateInline]