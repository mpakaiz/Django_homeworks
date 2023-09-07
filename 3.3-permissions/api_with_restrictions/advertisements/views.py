from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, Favourite
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer, FavouriteSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = AdvertisementFilter
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        user = self.request.user
        user_authorization = self.request.user.is_authenticated
        if user_authorization is True:
            print('User is authorized')
            return Advertisement.objects.all().filter(creator=user)
        return Advertisement.objects.all().exclude(status='DRAFT')


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []

class AddToFavouritesView(generics.CreateAPIView):
    serializer_class = FavouriteSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def create(self, request, *args, **kwargs):
        user = request.user
        advertisement_id = request.data.get("advertisement_id")

        try:
            advertisement = Advertisement.objects.get(pk=advertisement_id)

        except Advertisement.DoesNotExist:
            return Response({"error": 'Advertisement not found'}, status=status.HTTP_400_BAD_REQUEST)

        favourite = Favourite(user=user, advertisements=advertisement)
        favourite.save()

        return Response({"message: Advertisement added to favourites"}, status=status.HTTP_201_CREATED)



