from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm

@login_required
def liste_reservations(request):
    # Si l'utilisateur est un client, ne montrer que ses réservations
    if request.user.role == 'client':
        reservations = Reservation.objects.filter(client=request.user)
    else:
        # Pour le personnel, montrer toutes les réservations
        reservations = Reservation.objects.all()
    
    form = ReservationForm()
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user.role == 'client':
                reservation.client = request.user
            reservation.statut = 'confirmee'
            reservation.save()
            return redirect('reservations:liste_reservations')
    
    return render(request, 'reservations/liste_reservations.html', {
        'reservations': reservations,
        'form': form
    })

@login_required
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Réservation mise à jour avec succès.')
            return redirect('reservations:liste_reservations')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/update_reservation.html', {
        'form': form,
        'reservation': reservation
    })

@login_required
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Réservation supprimée avec succès.')
        return redirect('reservations:liste_reservations')
    return render(request, 'reservations/delete_reservation.html', {
        'reservation': reservation
    }) 