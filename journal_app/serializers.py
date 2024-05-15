from .models import TagsModel,JournalModel
from rest_framework import  serializers


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TagsModel
        fields='__all__'