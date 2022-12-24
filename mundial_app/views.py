from django.shortcuts import render
from mundial_api.models import Equipo
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def puntoProtegidoEjemplo(request):
    return Response ({'status':'ok'}, status=status.HTTP_200_OK)

def EquiposMundial(request):
    equipo = Equipo.objects.all()
    data = {'equipo': equipo}
    return render(request, 'mostrarEquipo.html', data)

def EquipoCampeon(request, id):
    equipo = Equipo.objects.filter(id=id).first()
    data = {'equipo': equipo}
    return render(request, 'mostrarCampeon.html', data)
