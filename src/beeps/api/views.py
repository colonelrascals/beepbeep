from rest_framework import generics
from django.db.models import Q

from beeps.models import Beep
from .serializers import BeepModelSerializer


class BeepListAPIView(generics.ListAPIView):
    serializer_class = BeepModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Beep.objects.all()
        query = self.request.GET.get('q', None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )

        return qs