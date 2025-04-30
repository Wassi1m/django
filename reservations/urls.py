from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.liste_reservations, name='liste_reservations'),
    path('<int:reservation_id>/update/', views.update_reservation, name='update_reservation'),
    path('<int:reservation_id>/delete/', views.delete_reservation, name='delete_reservation'),
] 