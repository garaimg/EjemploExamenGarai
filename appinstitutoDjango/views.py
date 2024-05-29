from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from appinstitutoDjango.forms import EstudianteForm, AsignaturaForm
from appinstitutoDjango.models import Estudiante, Asignatura


# Create your views here.
class EstudiantesListView(ListView):
    model = Estudiante
    template_name = "appinstitutoDjango/lista_estudiantes.html"
    context_object_name = 'estudiantes'

    def get_queryset(self):
        asignatura = get_object_or_404(Asignatura, id=self.kwargs['pk'])
        return Estudiante.objects.filter(asignatura=asignatura)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        asignatura = get_object_or_404(Asignatura, id=self.kwargs['pk'])
        context['asignatura'] = asignatura
        return context


class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = "appinstitutoDjango/detalle_estudiante.html"
    context_object_name = 'estudiante'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estudiante = self.get_object()
        context['asignaturas'] = estudiante.asignatura_set.all()
        return context


class AsignaturasListView(ListView):
    model = Asignatura
    template_name = "appinstitutoDjango/lista_asignaturas.html"
    context_object_name = 'asignaturas'


class AsignaturaDetailView(DetailView):
    model = Asignatura
    template_name = "appinstitutoDjango/detalle_asignatura.html"
    context_object_name = 'asignatura'


class EstudianteCreateView(View):
    def get(self, request):
        formulario = EstudianteForm()
        context = {'formulario': formulario}
        return render(request, 'appinstitutoDjango/crear_estudiante.html', context)

    def post(self, request):
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_asignaturas')

        return render(request, 'appinstitutoDjango/crear_estudiante.html', {'formulario': formulario})


class AsignaturaCreateView(View):
    def get(self, request):
        formulario = AsignaturaForm()
        context = {'formulario': formulario}
        return render(request, 'appinstitutoDjango/crear_asignatura.html', context)

    def post(self, request):
        formulario = AsignaturaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_asignaturas')

        return render(request, 'appinstitutoDjango/crear_asignatura.html', {'formulario': formulario})


class EstudianteUpdateView(UpdateView):
    model = Estudiante

    def get(self, request, pk):
        estudiante = Estudiante.objects.get(pk=pk)
        formulario = EstudianteForm(instance=estudiante)
        context = {
            'formulario': formulario,
            'estudiante': estudiante
        }
        return render(request, 'appinstitutoDjango/estudiante_update.html', context)

    # Llamada para procesar la actualización del departamento
    def post(self, request, pk):
        estudiante = Estudiante.objects.get(pk=pk)
        formulario = EstudianteForm(request.POST, instance=estudiante)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_estudiantes', estudiante.pk)
        else:
            formulario = EstudianteForm(instance=estudiante)
        return render(request, 'appinstitutoDjango/estudiante_update.html', {'formulario': formulario})


class AsignaturaUpdateView(UpdateView):
    model = Asignatura

    def get(self, request, pk):
        asignatura = Asignatura.objects.get(id=pk)
        formulario = AsignaturaForm(instance=asignatura)
        context = {
            'formulario': formulario,
            'asignatura': asignatura
        }
        return render(request, 'appinstitutoDjango/asignatura_update.html', context)

    def post(self, request, pk):
        asignatura = Asignatura.objects.get(id=pk)
        formulario = AsignaturaForm(request.POST, instance=asignatura)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_asignaturas', asignatura.pk)
        else:
            formulario = AsignaturaForm(instance=asignatura)
        return render(request, 'appinstitutoDjango/asignatura_update.html', {'formulario': formulario})


class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('lista_asignaturas')
    template_name = 'appinstitutoDjango/eliminar_estudiante.html'
    context_object_name = 'estudiante'


class AsignaturaDeleteView(DeleteView):
    model = Asignatura
    success_url = reverse_lazy('lista_asignaturas')
    template_name = 'appinstitutoDjango/eliminar_asignatura.html'
    context_object_name = 'asignatura'
