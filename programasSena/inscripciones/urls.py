from django.urls import path
from .views import UsuarioList, ProgramaList, inscritos_por_programa

urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name='usuario-list'),
    path('programas/', ProgramaList.as_view(), name='programa-list'),
     path('inscritos-por-programa/', inscritos_por_programa, name='inscritos-por-programa'),
   
]
