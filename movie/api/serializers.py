from rest_framework import serializers
from movie.models import StreamPlatForm, WatchList


class WatchListModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatFormModelSerializer(serializers.ModelSerializer):
    watchlist = WatchListModelSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatForm
        fields = "__all__"


