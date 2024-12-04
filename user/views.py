from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import User, Favourite
from .serializers import UserSerializer, FavouriteSerializer
from film.models import Film

class UserApiList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()

class UserAPIUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAPIDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FavoriteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        favorites = Favourite.objects.filter(user=request.user)
        serializer = FavouriteSerializer(favorites, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def add(self, request):
        film_id = request.data.get('film_id')
        try:
            film = Film.objects.get(id=film_id)
            Favourite.objects.create(user=request.user, film=film)
            return Response({'message': 'Success'}, status=status.HTTP_201_CREATED)
        except Film.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def remove(self, request):
        film_id = request.data.get('film_id')
        favorite = Favourite.objects.filter(user=request.user, film_id=film_id)
        if favorite.exists():
            favorite.delete()
            return Response({'message': 'Success'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)