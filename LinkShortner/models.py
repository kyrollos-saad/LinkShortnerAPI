from django.db import models

# Create your models here.
class Links(models.Model):
    slug = models.CharField(max_length = 6, primary_key = True)
    web = models.CharField(max_length = 255, unique = True)
    android_primary = models.CharField(max_length = 255, unique = True)
    android_fallback = models.CharField(max_length = 255, unique = True)
    ios_primary = models.CharField(max_length = 255, unique = True)
    ios_fallback = models.CharField(max_length = 255, unique = True)

    def __str__(self):
        return str(self.slug)

    class Meta:
        verbose_name_plural = 'Links'

