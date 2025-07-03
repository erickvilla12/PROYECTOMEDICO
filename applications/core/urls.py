from django.urls import path
from applications.core import views
from .views.historialclinico import HistorialClinicoCreateView, HistorialClinicoDeleteView, HistorialClinicoDetailView, HistorialClinicoListView, HistorialClinicoUpdateView
from applications.core.views.paciente import paciente_find, paciente_search_view

#importaciones para doctores
from applications.core.views.doctores import (
    DoctorListView,
    DoctorCreateView,
    DoctorUpdateView,
    DoctorDeleteView
)
app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Pacientes
    path('paciente_find/', paciente_find, name='paciente_find'),  # tu vista JSON AJAX
    path('pacientes/search/', paciente_search_view, name='paciente_search'), 
    path('historialclinico/', HistorialClinicoListView.as_view(), name='historialclinico_list'),
    path('historialclinico/create/', HistorialClinicoCreateView.as_view(), name='historialclinico_create'),
    path('historialclinico/<int:pk>/update/', HistorialClinicoUpdateView.as_view(), name='historialclinico_update'),
    path('historialclinico/<int:pk>/delete/', HistorialClinicoDeleteView.as_view(), name='historialclinico_delete'),
    path('historialclinico/<int:pk>/', HistorialClinicoDetailView.as_view(), name='historialclinico_detail'),
    
    #Rutas para doctores
    path('doctores/', DoctorListView.as_view(), name='doctor_list'),
    path('doctores/nuevo/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctores/editar/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctores/eliminar/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),
]



