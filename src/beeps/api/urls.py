from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
    BeepListAPIView
)
app_name='beep-api'
urlpatterns = [
    url(r'^$', BeepListAPIView.as_view(), name ='list'),
    
]