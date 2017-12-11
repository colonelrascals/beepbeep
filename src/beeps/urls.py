from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
    RebeepView,
    BeepListView, 
    BeepDetailView, 
    BeepCreateView, 
    BeepUpdateView,
    BeepDeleteView
)
app_name='beep'
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/')),
    url(r'^search/$', BeepListView.as_view(), name='list'),
    url(r'^create/$', BeepCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', BeepDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/rebeep/$', RebeepView.as_view(), name='detail'),    
    url(r'^(?P<pk>\d+)/edit/$', BeepUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/delete/$', BeepDeleteView.as_view(), name='delete'),


]