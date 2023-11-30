from django.shortcuts import render
from .serializers import PeliculaSerializer
from rest_framework import viewsets

# Create your views here.

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer