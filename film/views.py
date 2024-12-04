from .models import Film
from .serializers import FilmSerializer
from rest_framework import generics

class FilmApiList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmAPIUpdate(generics.UpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer