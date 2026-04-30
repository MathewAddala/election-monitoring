import os
from django.core.management.base import BaseCommand
from accounts.models import CustomUser


class Command(BaseCommand):
    help = 'Create default admin user if none exists'

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(role='admin').exists():
            username = os.environ.get('ADMIN_USERNAME', 'admin')
            password = os.environ.get('ADMIN_PASSWORD', 'ElectionWatch2026!')
            email = os.environ.get('ADMIN_EMAIL', 'admin@electionwatch.app')
            CustomUser.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                role='admin',
            )
            self.stdout.write(self.style.SUCCESS(f'Admin user "{username}" created.'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists, skipping.'))
