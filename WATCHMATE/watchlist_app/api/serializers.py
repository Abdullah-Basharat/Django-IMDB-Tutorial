from rest_framework import serializers

from ..models import WatchList, StreamPlatform, Review


# def validate_obj(value):
#     if len(value) < 3:
#         raise serializers.ValidationError("Movie is too short")
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[validate_obj])
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Movie` instance, given the validated data.
#         :param validated_data:
#         :return:
#         """
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Movie` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     #Field Level Validators
#     def validate_name(self,value):
#         if len(value) < 3:
#             raise serializers.ValidationError('Name must be at least 3 characters')
#         return value
#
#     #Object Level Validaotrs
#     def validate(self,data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description must be different')
#         return data

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()



    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['id','created','updated','reviewer']

    def get_review_user(self, obj):
        return obj.reviewer.username

    def get_movie(self, obj):
        return obj.movie.title


class WatchListSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['name','description']         #Fields to display
        # exclude = ['id']

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'
    # )
    watchlist = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'