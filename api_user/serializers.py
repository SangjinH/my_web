from rest_framework import serializers
from api_user.models import User
from api_article.models import Article

class UserSerializer(serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    # ======= serializers.ModelSerializer 
    class Meta:
        model = User
        fields = ['id', 'user_id', 'author']



    #======== serializers.Serializers 쓸때

    # def create(self, validated_data):
    #     """
    #     Create and return a new 'User' instance, given the validated data.
    #     """
    #     print('validated 데이터는 : ', data)
    #     return User.objects.create(data)
    

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing 'User' instance, given the validated data.
    #     """
    #     instance.user_id = validated_data.get('user_id', instance.user_id)
    #     instance.password = validated_data.get('password', instance.password)
    #     instance.address = validated_data.get('address', instance.address)