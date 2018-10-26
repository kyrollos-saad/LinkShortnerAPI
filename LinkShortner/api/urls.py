from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^create/$', view = ShortnerCreate.as_view()),
    url(r'^update/(?P<slug>\S+)/$', view = ShortnerUpdate.as_view()),
    url(r'^(?P<slug>\S+)/$', view = ShortnerRetrieve.as_view()),
]
