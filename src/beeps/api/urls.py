from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
    LikeToggleAPIView,
    RebeepAPIView,
    BeepListAPIView,
    BeepCreateView
)
app_name='beep-api'
urlpatterns = [
    url(r'^$', BeepListAPIView.as_view(), name ='list'),
    url(r'^create/$', BeepCreateView.as_view(), name ='create'),
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'),
    url(r'^(?P<pk>\d+)/rebeep/$', RebeepAPIView.as_view(), name='rebeep'),

]
