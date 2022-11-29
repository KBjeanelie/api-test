from rest_framework import serializers

from .models import Livre

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livre
        fields = [
            'id',
            'category',
            'titre',
            'auteur',
            'nombreDePage',
            'description',
            'prix',
            'created_at',
            'updated_at']