from rest_framework import serializers


class LogInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    client_id = serializers.CharField()
    client_secret = serializers.CharField()


class RefreshSerializer(serializers.Serializer):
    client_id = serializers.CharField()
    client_secret = serializers.CharField()

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()