from rest_framework import serializers
from .models import PenulisanIlmiah
from django.contrib.auth.models import User


class PenulisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PenulisanIlmiah
        fields = ['id', 'judul_PI', 'nama', 'keterangan_Sidang']
