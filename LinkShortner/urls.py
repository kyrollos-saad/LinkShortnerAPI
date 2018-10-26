from django.conf.urls import url
from .views import *

app_name = 'link_shortner'

urlpatterns = [
    url(r'^login/$', login_view, name ='login_view'),
    url(r'^login/out/$', logout_view, name ='logout_view'),
    url(r'^create/$', create_short_link, name ='create_shortlink_view'),
]
