from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^create/$', view = ShortnerC.as_view()),
    url(r'^(?P<slug>\S+)/$', view = ShortnerRU.as_view()),
]

