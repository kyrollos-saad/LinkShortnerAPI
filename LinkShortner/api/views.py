from rest_framework import generics
from LinkShortner.models import Links

class ShortnerRU(generics.RetrieveUpdateAPIView):  # R: retrieve, U: update
    lookup_field = 'slug'

    def get_queryset(self):
        return Links.objects.all()

    # this is an override. the default will do just fine assuming that we don't need to retrieve by anything other than the slug
    # def get_object(self, **kwargs):
    #     pass
