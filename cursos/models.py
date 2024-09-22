from django.db import models

# Create your models here.
class Cursos(models.Model):
    name = models.CharField(max_length=100)  # Campo para el nombre del curso
    description = models.TextField()  # Campo para la descripción del curso
    start_date = models.DateField()  # Campo para la fecha de inicio del curso

    def __str__(self):
        return self.name
