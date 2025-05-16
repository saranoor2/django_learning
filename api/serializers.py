from rest_framework import serializers
from .models import Ad

# class AdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ad
#         # fields = '__all__'
#         fields = ('title', 'type')

class AdSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Ad.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance