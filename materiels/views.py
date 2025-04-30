from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Materiel
from .forms import MaterielForm

@login_required
def liste_materiels(request):
    materiels = Materiel.objects.all()
    form = MaterielForm()
    
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materiels:liste_materiels')
    
    return render(request, 'materiels/liste_materiels.html', {
        'materiels': materiels,
        'form': form
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