from rest_framework import serializers


class MemberProfileSerializer(serializers.Serializer):
    role = serializers.CharField(required=False)
    emailEnabled = serializers.BooleanField(required=False)
    timezone = serializers.CharField(required=False, allow_blank=True)
