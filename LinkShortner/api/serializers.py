from rest_framework import serializers
from LinkShortner.models import Links

class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = [
            'slug',
            'web',
            'android_primary',
            'android_fallback',
            'ios_primary',
            'ios_fallback',
        ]
