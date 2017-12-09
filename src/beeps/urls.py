from django.conf.urls import url


from .views import BeepListView, BeepDetailView, BeepCreateView

urlpatterns = [
    url(r'^$', BeepListView.as_view(), name='list'),
    url(r'^create/$', BeepCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', BeepDetailView.as_view(), name='detail'),
]