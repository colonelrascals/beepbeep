from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from beeps.models import Beep


class BeepModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    is_rebeep = serializers.SerializerMethodField()
    class Meta:
        model = Beep
        fields = [
            'id',
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
            'is_rebeep'
        ]

    def get_is_rebeep(self, obj):
        if obj.parent:
            return True
        return False

    def get_date_display(self, obj):
        return obj.timestamp.strftime('%b %d %I:%M %p')

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + ' ago'
