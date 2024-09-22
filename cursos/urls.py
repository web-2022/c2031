from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list_view, name='course_list'),  # Ruta para la lista de cursos
    path('<int:id>/', views.course_detail_view, name='course_detail'),  # Ruta para los detalles del curso
]
