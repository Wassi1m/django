from django.urls import path
from . import views

app_name = 'etages'

urlpatterns = [
    path('', views.liste_etages, name='liste_etages'),
    path('<int:etage_id>/update/', views.update_etage, name='update_etage'),
    path('<int:etage_id>/delete/', views.delete_etage, name='delete_etage'),
] 