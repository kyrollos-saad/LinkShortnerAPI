from rest_framework import generics
from LinkShortner.models import Links
from .serializers import LinksSerializer


class ShortnerRU(generics.RetrieveUpdateAPIView):  # R: retrieve, U: update
    lookup_field = 'slug'
    serializer_class = LinksSerializer

    def get_queryset(self):
        print('-'*100)
        print('self.request.user:', self.request.user)
        print('self.request.auth:', self.request.auth)
        print('-'*100)
        return Links.objects.all()

    # this is an override. the default will do just fine assuming that we don't need to retrieve by anything other than the slug
    # def get_object(self, **kwargs):
    #     pass


class ShortnerC(generics.CreateAPIView):  # C: create
    serializer_class = LinksSerializer

    def get_queryset(self):
        return Links.objects.all()
