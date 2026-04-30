from django.db import models
from django.conf import settings
from elections.models import Election


class IssueReport(models.Model):
    SEVERITY_CHOICES = [
        ('low',    'Low'),
        ('medium', 'Medium'),
        ('high',   'High'),
    ]
    STATUS_CHOICES = [
        ('pending',  'Pending'),
        ('reviewed', 'Reviewed'),
        ('resolved', 'Resolved'),
    ]
    citizen     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')
    election    = models.ForeignKey(Election, on_delete=models.CASCADE, related_name='reports')
    title       = models.CharField(max_length=200)
    description = models.TextField()
    severity    = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='low')
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    evidence    = models.ImageField(upload_to='evidence/', blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self): return self.title