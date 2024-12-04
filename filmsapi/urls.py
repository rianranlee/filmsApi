from django.urls import path
from user.views import UserApiList, UserAPIUpdate, UserAPIDelete, FavoriteViewSet
from film.views import FilmApiList, FilmAPIUpdate

urlpatterns = [
    path('api/films/', FilmApiList.as_view()),
    path('api/films/edit/<int:pk>/', FilmAPIUpdate.as_view()),

    path('api/users/', UserApiList.as_view()),
    path('api/users/edit/<int:pk>/', UserAPIUpdate.as_view()),
    path('api/users/delete/<int:pk>/', UserAPIDelete.as_view()),

    path('api/favorites/', FavoriteViewSet.as_view({'get': 'list', 'post': 'add'})),
    path('api/favorites/remove/', FavoriteViewSet.as_view({'post': 'remove'})),
]
