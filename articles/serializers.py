from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'publication_date', 'author']

    def validate(self, data):
        title = data.get('title')
        content = data.get('content')
        author = data.get('author')

        if not title:
            raise serializers.ValidationError("Title cannot be empty.")
        if not content:
            raise serializers.ValidationError("Content cannot be empty.")
        if not author:
            raise serializers.ValidationError("Author cannot be empty.")
        
        # Add additional validation for publication_date if needed

        return data
