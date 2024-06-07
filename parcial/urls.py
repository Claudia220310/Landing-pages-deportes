from django.urls import path
from . import views


urlpatterns = [
    path('', views.paginaPrincipal, name='index'),  
    path('ver-mas/<int:deporte_id>/', views.var_mas, name='ver_mas'), 
    path('contenido.html',views.contenido, name='contenido'),
    
]
