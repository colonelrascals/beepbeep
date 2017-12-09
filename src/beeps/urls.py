from django.conf.urls import url


from .views import (
    BeepListView, 
    BeepDetailView, 
    BeepCreateView, 
    BeepUpdateView,
    BeepDeleteView
)

urlpatterns = [
    url(r'^$', BeepListView.as_view(), name='list'),
    url(r'^create/$', BeepCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', BeepDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', BeepUpdateView.as_view(), name='edit'),
        url(r'^(?P<pk>\d+)/delete/$', BeepDeleteView.as_view(), name='delete'),


]