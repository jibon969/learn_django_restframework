from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
