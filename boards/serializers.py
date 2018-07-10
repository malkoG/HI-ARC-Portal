from rest_framework import serializers
from boards.models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    description = serializers.CharField(required=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description')

    def create(self, validated_data):
        """
        Create and return a new `Post` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Post` instance, given the validated data.
        """

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('title', instance.description)
        instance.save()
        return instance