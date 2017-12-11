from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from beeps.models import Beep

class BeepModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    class Meta:
        model = Beep
        fields = [
            'user',
            'content'
        ]