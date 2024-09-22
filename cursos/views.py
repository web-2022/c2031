from django.shortcuts import render, get_object_or_404
from .models import Cursos

# Create your views here.
def course_list_view(request):
    courses = Cursos.objects.all()  # Obtiene todos los cursos de la base de datos
    return render(request, 'cursos/course_list.html', {'courses': courses})

def course_detail_view(request, id):
    course = get_object_or_404(Cursos, id=id)  # Obtiene un curso por su ID o devuelve 404 si no existe
    return render(request, 'cursos/course_detail.html', {'course': course})

def ingresa(request):
    return render(request,)