from django.urls import path

from . import views

app_name = 'animais'

urlpatterns = [
    path('', views.listaranimais, name='listaranimais'),
    path('tipos/', views.listatipoanimal, name='listatipoanimal'),
    path('tipos/<int:tipo_id>/racas/', views.listaracas, name='listaracas'),
]