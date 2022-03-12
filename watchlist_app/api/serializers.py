from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'active']

    # Field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is to short")
        return value

    # Object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name & description must be different")
        return data


"""
def validate_description(value):
    if len(value) < 2:
        raise serializers.ValidationError("Description is to short")
    return value


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(validators=[validate_description])  # validators
    active = serializers.BooleanField()

    class Meta:
        model = Movie
        fields = ('id', 'name', 'description', 'active')

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.active = validated_data.get('active')
        instance.save()
        return instance

    # Field level validation

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is to short")
        return value

    # Object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name & description must be different")
        return data
"""