from rest_framework import serializers

from ..models import Movie

def validate_obj(value):
    if len(value) < 3:
        raise serializers.ValidationError("Movie is too short")
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(validators=[validate_obj])
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        """
        Create and return a new `Movie` instance, given the validated data.
        :param validated_data:
        :return:
        """
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Movie` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    #Field Level Validators
    def validate_name(self,value):
        if len(value) < 3:
            raise serializers.ValidationError('Name must be at least 3 characters')
        return value

    #Object Level Validaotrs
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and Description must be different')
        return data
