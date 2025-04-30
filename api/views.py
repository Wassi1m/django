from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Etage
from .forms import EtageForm
from .models import Materiel
from .forms import MaterielForm

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

@login_required
def update_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    if request.method == 'POST':
        form = MaterielForm(request.POST, instance=materiel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Matériel mis à jour avec succès.')
            return redirect('materiels:liste_materiels')
    else:
        form = MaterielForm(instance=materiel)
    return render(request, 'materiels/update_materiel.html', {
        'form': form,
        'materiel': materiel
    })

@login_required
def delete_materiel(request, materiel_id):
    materiel = get_object_or_404(Materiel, id=materiel_id)
    if request.method == 'POST':
        materiel.delete()
        messages.success(request, 'Matériel supprimé avec succès.')
        return redirect('materiels:liste_materiels')
    return render(request, 'materiels/delete_materiel.html', {
        'materiel': materiel
    }) 