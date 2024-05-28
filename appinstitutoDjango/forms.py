from django import forms

from appinstitutoDjango.models import Estudiante, Asignatura


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = '__all__'
