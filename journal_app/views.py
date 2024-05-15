from django.shortcuts import render
from .serializers import TagsSerializer
from .models import  TagsModel,JournalModel
from rest_framework.viewsets import  ModelViewSet
from .permissions import IsAdminOrReadOnly



class TagsView(ModelViewSet):
    queryset = TagsModel.objects.all()
    serializer_class = TagsSerializer
    permission_classes = [IsAdminOrReadOnly]
