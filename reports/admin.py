from django.contrib import admin
from .models import IssueReport


@admin.register(IssueReport)
class IssueReportAdmin(admin.ModelAdmin):
    list_display    = ['title', 'citizen', 'election', 'severity', 'status', 'created_at']
    list_filter     = ['severity', 'status']
    search_fields   = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']