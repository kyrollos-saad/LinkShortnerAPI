from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from LinkShortner.models import Links
from .serializers import LinksSerializer


class ShortnerRetrieve(generics.RetrieveAPIView):  # R: retrieve
    lookup_field = 'slug'
    serializer_class = LinksSerializer

    def get_queryset(self):
        print('-'*70 + '>', self.request.user)
        return Links.objects.all()

    # this is an override. the default will do just fine assuming that we don't need to retrieve by anything other than the slug
    # def get_object(self, **kwargs):
    #     pass


class ShortnerUpdate(generics.UpdateAPIView):  # U: update
    lookup_field = 'slug'
    serializer_class = LinksSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Links.objects.all()


class ShortnerCreate(generics.CreateAPIView):  # C: create
    serializer_class = LinksSerializer

    def get_queryset(self):
        return Links.objects.all()
