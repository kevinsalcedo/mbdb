from rest_framework import serializers
from .models import Disorder, Story, BlogPost, LocalResource

class DisorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disorder
        fields = ('id', 'name')

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'title', 'content', 'date_created', 'date_modified', 'author', 'disorder')
        read_only_fields = ('date_created', 'date_modified')

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'content', 'date_created', 'author', 'disorder')
        read_only_fields = ('date_created',)

class LocalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalResource
        fields = ('id','name','img_url','url','address','phone','description','disorder')
