from rest_framework import serializers
from .models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['id', 'titulo', 'ano', 'genero']
        read_only_fields = ['id']