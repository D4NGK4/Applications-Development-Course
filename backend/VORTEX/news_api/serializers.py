from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    url = serializers.URLField()
    urlToImage = serializers.URLField()
    publishedAt = serializers.DateTimeField()

class NewsSerializer(serializers.Serializer):
    articles = ArticleSerializer(many=True)