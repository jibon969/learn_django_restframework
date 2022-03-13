from rest_framework import serializers
from movie.models import StreamPlatForm, WatchList, Review


class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class WatchListModelSerializer(serializers.ModelSerializer):
    review = ReviewModelSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatFormModelSerializer(serializers.ModelSerializer):
    watchlist = WatchListModelSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatForm
        fields = "__all__"





