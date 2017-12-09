from django.conf.urls import url


from .views import BeepListView, BeepDetailView

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', BeepListView.as_view(), name='list'),
    url(r'^1/$', BeepDetailView.as_view(), name='detail'),
]