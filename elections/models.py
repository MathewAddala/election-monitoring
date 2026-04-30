from django.db import models


class Election(models.Model):
    STATUS_CHOICES = [
        ('upcoming',  'Upcoming'),
        ('ongoing',   'Ongoing'),
        ('completed', 'Completed'),
    ]
    title         = models.CharField(max_length=200)
    description   = models.TextField()
    election_date = models.DateField()
    location      = models.CharField(max_length=200)
    status        = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-election_date']

    def __str__(self): return self.title


class ElectionUpdate(models.Model):
    election  = models.ForeignKey(Election, on_delete=models.CASCADE, related_name='updates')
    message   = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self): return f'Update → {self.election.title}'