from django.shortcuts import render, redirect, get_object_or_404
from .models import Chambre, TypeChambre
from .forms import ChambreForm, TypeChambreForm
from users.decorators import login_required_message

@login_required_message
def liste_chambres(request):
    chambres = Chambre.objects.all()
    form = ChambreForm()
    type_form = TypeChambreForm()
    
    if request.method == 'POST':
        if 'chambre_form' in request.POST:
            form = ChambreForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('chambres:liste_chambres')
        elif 'type_form' in request.POST:
            type_form = TypeChambreForm(request.POST)
            if type_form.is_valid():
                type_form.save()
                return redirect('chambres:liste_chambres')
    
    return render(request, 'chambres/liste_chambres.html', {
        'chambres': chambres,
        'form': form,
        'type_form': type_form
    })

def detail_chambre(request, chambre_id):
    chambre = get_object_or_404(Chambre, id=chambre_id)
    return render(request, 'chambres/detail_chambre.html', {'chambre': chambre}) 