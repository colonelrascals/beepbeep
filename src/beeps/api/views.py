from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from beeps.models import Beep
from .pagination import StandardResultsPagination
from .serializers import BeepModelSerializer


class BeepCreateView(generics.CreateAPIView):
    serializer_class = BeepModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BeepListAPIView(generics.ListAPIView):
    serializer_class = BeepModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(BeepListAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self, *args, **kwargs):
        requested_user = self.kwargs.get("username")

        if requested_user:
            qs = Beep.objects.filter(user__username=requested_user).order_by("-timestamp")
        else:
            im_following = self.request.user.profile.get_following() # none
            qs1 = Beep.objects.filter(user__in=im_following)
            qs2 = Beep.objects.filter(user=self.request.user)
            qs = (qs1 | qs2).distinct().order_by("-timestamp")

        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs

class SearchAPIView(generics.ListAPIView):
    serializer_class = BeepModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        qs = Beep.objects.all().order_by("-timestamp")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs


class RebeepAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        beep_qs = Beep.objects.filter(pk=pk)
        message = "Not allowed"
        if beep_qs.exists() and beep_qs.count() == 1:
            # if request.user.is_authenticated():
            new_beep = Beep.objects.rebeep(request.user, beep_qs.first())
            if new_beep is not None:
                data = BeepModelSerializer(new_beep).data
                return Response(data)
            message = "Cannot rebeep the same in 1 day"
        return Response({"message": message}, status=400)

class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        tweet_qs = Beep.objects.filter(pk=pk)
        message = "Not allowed"
        if request.user.is_authenticated:
            is_liked = Beep.objects.like_toggle(request.user, tweet_qs.first())
            return Response({'liked': is_liked})
        return Response({"message": message}, status=400)
