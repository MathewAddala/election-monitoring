from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from elections.models import Election
from reports.models import IssueReport
from accounts.models import CustomUser


@login_required
def home(request):
    user = request.user

    if user.is_admin:
        context = {
            'role': 'admin',
            'total_elections':  Election.objects.count(),
            'upcoming':         Election.objects.filter(status='upcoming').count(),
            'ongoing':          Election.objects.filter(status='ongoing').count(),
            'completed':        Election.objects.filter(status='completed').count(),
            'total_reports':    IssueReport.objects.count(),
            'pending_reports':  IssueReport.objects.filter(status='pending').count(),
            'high_severity':    IssueReport.objects.filter(severity='high').count(),
            'total_citizens':   CustomUser.objects.filter(role='citizen').count(),
            'recent_elections': Election.objects.order_by('-created_at')[:5],
            'recent_reports':   IssueReport.objects.order_by('-created_at')[:5],
        }

    elif user.is_observer:
        context = {
            'role': 'observer',
            'total_elections':  Election.objects.count(),
            'ongoing':          Election.objects.filter(status='ongoing').count(),
            'total_reports':    IssueReport.objects.count(),
            'pending_reports':  IssueReport.objects.filter(status='pending').count(),
            'high_severity':    IssueReport.objects.filter(severity='high').count(),
            'recent_reports':   IssueReport.objects.order_by('-created_at')[:5],
        }

    else:  # citizen
        context = {
            'role': 'citizen',
            'my_reports':       IssueReport.objects.filter(citizen=user).count(),
            'my_pending':       IssueReport.objects.filter(citizen=user, status='pending').count(),
            'my_resolved':      IssueReport.objects.filter(citizen=user, status='resolved').count(),
            'recent_elections': Election.objects.order_by('-election_date')[:5],
            'my_recent_reports': IssueReport.objects.filter(citizen=user).order_by('-created_at')[:5],
        }

    return render(request, 'dashboard/home.html', context)