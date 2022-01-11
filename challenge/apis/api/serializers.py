from rest_framework import serializers

from apis.models import Apis

class ApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apis
        fields = '__all__'