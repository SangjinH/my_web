from rest_framework import serializers
from api_article.models import Article

class ArticleSerializer(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source='name.user_id')

    class Meta:
        model = Article
        fields = ['name', 'title', 'content']