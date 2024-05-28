from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    DNI = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.DNI

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['DNI']


class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.IntegerField()
    estudiante = models.ManyToManyField(Estudiante)  # N-M

    def __str__(self):
        return f"{self.nombre} -- {self.creditos}"

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        ordering = ['nombre']
