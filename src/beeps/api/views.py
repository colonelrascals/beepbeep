from rest_framework import generics, permissions
from django.db.models import Q
from beeps.models import Beep
from .pagination import StandardResultsPagination
from .serializers import BeepModelSerializer


class BeepCreateView(generics.CreateAPIView):
    serializer_class = BeepModelSerializer
    permission_classes= [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BeepListAPIView(generics.ListAPIView):
    serializer_class = BeepModelSerializer
    pagination_class = StandardResultsPagination
    def get_queryset(self, *args, **kwargs):
        qs = Beep.objects.all().order_by('-timestamp')
        query = self.request.GET.get('q', None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )

        return qs
