from rest_framework import serializers
from .models import Snack,Post

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields =['id','owner', 'name', 'desc']
        # fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__' 