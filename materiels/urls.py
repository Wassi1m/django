from django.urls import path
from . import views

app_name = 'materiels'

urlpatterns = [
    path('', views.liste_materiels, name='liste_materiels'),
    path('<int:materiel_id>/update/', views.update_materiel, name='update_materiel'),
    path('<int:materiel_id>/delete/', views.delete_materiel, name='delete_materiel'),
] 