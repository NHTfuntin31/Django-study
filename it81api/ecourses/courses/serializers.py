from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Course, Tag, Lesson, User



class UserSerializer(ModelSerializer):
    avatar = serializers.ImageField(required=False, allow_null=True)
    class Meta:
        model = User
        fields = ["id","first_name", "last_name", "email", "username", "password", "avatar"]
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }
        
    def create(self, validated_data):
        avatar_data = validated_data.pop('avatar', None)
        user = User(**validated_data)
        # user.first_name = validated_data['first_name']
        # user.last_name = validated_data['last_name']
        if avatar_data is not None:
            user.avatar = avatar_data
        user.set_password(validated_data['password'])
        
        user.save()
        return user


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "subject", "image", "created_date", "category"]
        
        
class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]
        
        
class LessonSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Lesson
        fields = ["id", "subject", "content", "created_date", "image","course", "tags"]