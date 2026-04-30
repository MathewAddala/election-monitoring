from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import IssueReport
from .forms import IssueReportForm

VALID_STATUSES = ['pending', 'reviewed', 'resolved']


@login_required
def report_list(request):
    if request.user.is_admin or request.user.is_observer:
        reports = IssueReport.objects.select_related('citizen', 'election').all()
    else:
        reports = IssueReport.objects.filter(citizen=request.user)
    severity = request.GET.get('severity', '')
    if severity:
        reports = reports.filter(severity=severity)
    return render(request, 'reports/list.html', {'reports': reports})


@login_required
def report_create(request):
    # Fix 4 — only citizens can file reports
    if not request.user.is_citizen:
        messages.error(request, 'Only citizens can file reports.')
        return redirect('reports:list')
    form = IssueReportForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        report = form.save(commit=False)
        report.citizen = request.user
        report.save()
        messages.success(request, 'Issue reported successfully.')
        return redirect('reports:list')
    return render(request, 'reports/create.html', {'form': form})


@login_required
def report_detail(request, pk):
    report = get_object_or_404(IssueReport, pk=pk)
    # Fix 3 — citizens can only see their own reports
    if request.user.is_citizen and report.citizen != request.user:
        messages.error(request, 'You can only view your own reports.')
        return redirect('reports:list')
    return render(request, 'reports/detail.html', {'report': report})


@login_required
def update_status(request, pk):
    if not (request.user.is_admin or request.user.is_observer):
        messages.error(request, 'Permission denied.')
        return redirect('reports:list')
    report = get_object_or_404(IssueReport, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status', '')
        # Fix 2 — validate against allowed values only
        if new_status in VALID_STATUSES:
            report.status = new_status
            report.save()
            messages.success(request, 'Status updated.')
        else:
            messages.error(request, 'Invalid status value.')
    return redirect('reports:detail', pk=pk)