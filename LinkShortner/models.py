from django.db import models
from random import randint


# Create your models here.
class Links(models.Model):
    def generate_slug():
        slug = ''
        for i in range(6):
            rand_char = chr(randint(48, 122))
            while not rand_char.isalnum():  # if the random char is alphanumeric try again indefinitely
                rand_char = chr(randint(48, 122))
            slug += rand_char
        if not Links.objects.filter(slug__iexact=slug):  # if filter returns []. or in other words if that random slug doesn't exist
            return slug

    slug = models.CharField(max_length = 6, primary_key = True, default = generate_slug, editable = False)
    web = models.CharField(max_length = 255)
    android_primary = models.CharField(max_length = 255)
    android_fallback = models.CharField(max_length = 255)
    ios_primary = models.CharField(max_length = 255)
    ios_fallback = models.CharField(max_length = 255)

    def __str__(self):
        return str(self.slug)

    class Meta:
        verbose_name_plural = 'Links'

