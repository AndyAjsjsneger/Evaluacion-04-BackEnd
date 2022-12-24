from django.urls import path
from mundial_app import views

urlpatterns = [
    path('equiposMundial', views.EquiposMundial),
    path('equipoCampeon/<int:id>', views.EquipoCampeon)
]