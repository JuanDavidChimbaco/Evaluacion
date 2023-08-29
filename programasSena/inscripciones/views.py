from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import render
from django.db.models import Count

from .models import Usuario, Programa
from .serializers import UsuarioSerializer, ProgramaSerializer
# Create your views here.


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProgramaList(generics.ListCreateAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    
    
@api_view(['GET'])
def inscritos_por_programa(request):
    programas_con_inscritos = Programa.objects.annotate(num_inscritos=Count('usuario'))

    data = [
        {
            'programa_nombre': programa.nombre,
            'cantidad_inscritos': programa.num_inscritos
        }
        for programa in programas_con_inscritos
    ]

    return Response(data)