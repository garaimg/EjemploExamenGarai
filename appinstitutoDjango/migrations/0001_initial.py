# Generated by Django 5.0.6 on 2024-05-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('DNI', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'ordering': ['DNI'],
            },
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.IntegerField()),
                ('estudiante', models.ManyToManyField(to='appinstitutoDjango.estudiante')),
            ],
            options={
                'verbose_name': 'Asignatura',
                'verbose_name_plural': 'Asignaturas',
                'ordering': ['nombre'],
            },
        ),
    ]
