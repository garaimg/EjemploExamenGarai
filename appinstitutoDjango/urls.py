"""
URL configuration for institutoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import AsignaturasListView, AsignaturaDetailView, EstudiantesListView, EstudianteDetailView, \
    EstudianteCreateView, AsignaturaCreateView, EstudianteUpdateView, AsignaturaUpdateView, EstudianteDeleteView, \
    AsignaturaDeleteView

urlpatterns = [
    path('', AsignaturasListView.as_view(), name='lista_asignaturas'),
    path('asignatura/<int:pk>', AsignaturaDetailView.as_view(), name='detalle_asignaturas'),
    path('asignatura/<int:pk>/estudiantes/', EstudiantesListView.as_view(), name='lista_estudiantes'),
    path('estudiante/<str:pk>', EstudianteDetailView.as_view(), name='detalle_estudiantes'),
    path('asignatura/create/', AsignaturaCreateView.as_view(), name='crear_asignatura'),
    path('estudiante/create/', EstudianteCreateView.as_view(), name='crear_estudiante'),
    path('estudiante/update/<str:pk>', EstudianteUpdateView.as_view(), name='editar_estudiante'),
    path('asignatura/update/<int:pk>', AsignaturaUpdateView.as_view(), name='editar_asignatura'),
    path('estudiante/delete/<str:pk>', EstudianteDeleteView.as_view(), name='eliminar_estudiante'),
    path('asignatura/delete/<int:pk>', AsignaturaDeleteView.as_view(), name='eliminar_asignatura'),
]
