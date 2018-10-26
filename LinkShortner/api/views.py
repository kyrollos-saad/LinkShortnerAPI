from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from LinkShortner.models import Links
from .serializers import LinksSerializer


class ShortnerRetrieveUpdate(generics.RetrieveUpdateAPIView):  # R: retrieve
    lookup_field = 'slug'
    serializer_class = LinksSerializer

    def get_queryset(self):
        return Links.objects.all()

    # this is an override. the default will do just fine assuming that we don't need to retrieve by anything other than the slug
    # def get_object(self, **kwargs):
    #     pass

    def put(self, request, *args, **kwargs):
        item_to_update = Links.objects.get(slug=kwargs['slug'])
        for key in request.data:
            if key == 'web':
                item_to_update.web = request.data[key]
            elif key == 'android_primary':
                item_to_update.android_primary = request.data[key]
            elif key == 'android_fallback':
                item_to_update.android_fallback = request.data[key]
            elif key == 'ios_primary':
                item_to_update.ios_primary = request.data[key]
            elif key == 'ios_fallback':
                item_to_update.ios_fallback = request.data[key]
        item_to_update.save()
        return Response(
            status = status.HTTP_200_OK,
            content_type = 'application/json',
            data = {
                "slug" : item_to_update.slug,
                "web" : item_to_update.web,
                "android_primary" : item_to_update.android_primary,
                "android_fallback" : item_to_update.android_fallback,
                "ios_primary" : item_to_update.ios_primary,
                "ios_fallback" : item_to_update.ios_fallback
            })


class ShortnerUpdate(generics.UpdateAPIView):  # U: update
    lookup_field = 'slug'
    serializer_class = LinksSerializer
    # permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        item_to_update = Links.objects.get(slug=kwargs['slug'])
        for key in request.data:
            if key == 'web':
                item_to_update.web = request.data[key]
            elif key == 'android_primary':
                item_to_update.android_primary = request.data[key]
            elif key == 'android_fallback':
                item_to_update.android_fallback = request.data[key]
            elif key == 'ios_primary':
                item_to_update.ios_primary = request.data[key]
            elif key == 'ios_fallback':
                item_to_update.ios_fallback = request.data[key]
        item_to_update.save()
        return Response(
            status = status.HTTP_200_OK,
            content_type = 'application/json',
            data = {
                "slug" : item_to_update.slug,
                "web" : item_to_update.web,
                "android_primary" : item_to_update.android_primary,
                "android_fallback" : item_to_update.android_fallback,
                "ios_primary" : item_to_update.ios_primary,
                "ios_fallback" : item_to_update.ios_fallback
            })

    def get_queryset(self):
        return Links.objects.all()


class ShortnerCreate(generics.ListCreateAPIView):
    serializer_class = LinksSerializer

    def get_queryset(self):
        print('-'*70 + '>', self.request.user)
        print('-'*70 + '>', self.request.auth)
        return Links.objects.all()
