from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Etage
from .forms import EtageForm

@login_required
def liste_etages(request):
    etages = Etage.objects.all()
    form = EtageForm()
    
    if request.method == 'POST':
        form = EtageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etages:liste_etages')
    
    return render(request, 'etages/liste_etages.html', {
        'etages': etages,
        'form': form
    })

@login_required
def update_etage(request, etage_id):
    etage = get_object_or_404(Etage, id=etage_id)
    if request.method == 'POST':
        form = EtageForm(request.POST, instance=etage)
        if form.is_valid():
            form.save()
            messages.success(request, 'Étage mis à jour avec succès.')
            return redirect('etages:liste_etages')
    else:
        form = EtageForm(instance=etage)
    return render(request, 'etages/update_etage.html', {
        'form': form,
        'etage': etage
    })

@login_required
def delete_etage(request, etage_id):
    etage = get_object_or_404(Etage, id=etage_id)
    if request.method == 'POST':
        etage.delete()
        messages.success(request, 'Étage supprimé avec succès.')
        return redirect('etages:liste_etages')
    return render(request, 'etages/delete_etage.html', {
        'etage': etage
    }) 