from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
    RebeepAPIView,
    BeepListAPIView,
    BeepCreateView
)
app_name='beep-api'
urlpatterns = [
    url(r'^$', BeepListAPIView.as_view(), name ='list'),
    url(r'^(?P<pk>\d+)/rebeep/$', RebeepAPIView.as_view(), name='rebeep'),
    url(r'^create/$', BeepCreateView.as_view(), name ='create'),
    
]