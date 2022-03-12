from rest_framework import serializers
from movie.models import StreamPlatForm, WatchList


class StreamPlatFormModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatForm
        fields = "__all__"


class WatchListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchList
        fields = "__all__"

