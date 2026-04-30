from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Election
from .forms import ElectionForm, ElectionUpdateForm


def election_list(request):
    status    = request.GET.get('status', '')
    elections = Election.objects.all()
    if status:
        elections = elections.filter(status=status)
    return render(request, 'elections/list.html', {'elections': elections, 'status': status})


def election_detail(request, pk):
    election    = get_object_or_404(Election, pk=pk)
    updates     = election.updates.all()
    update_form = ElectionUpdateForm()
    if request.method == 'POST' and request.user.is_authenticated and request.user.is_admin:
        update_form = ElectionUpdateForm(request.POST)
        if update_form.is_valid():
            upd = update_form.save(commit=False)
            upd.election = election
            upd.save()
            messages.success(request, 'Update posted.')
            return redirect('elections:detail', pk=pk)
    return render(request, 'elections/detail.html',
                  {'election': election, 'updates': updates, 'update_form': update_form})


@login_required
def election_create(request):
    if not request.user.is_admin:
        messages.error(request, 'Only admins can create elections.')
        return redirect('elections:list')
    form = ElectionForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Election created successfully.')
        return redirect('elections:list')
    return render(request, 'elections/create.html', {'form': form})


@login_required
def election_update(request, pk):
    if not request.user.is_admin:
        return redirect('elections:list')
    election = get_object_or_404(Election, pk=pk)
    form = ElectionForm(request.POST or None, instance=election)
    if form.is_valid():
        form.save()
        messages.success(request, 'Election updated.')
        return redirect('elections:detail', pk=pk)
    return render(request, 'elections/create.html', {'form': form, 'edit': True})