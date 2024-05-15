from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TagsView

router=DefaultRouter()

router.register(r'tags',TagsView,basename='tags')

urlpatterns=router.urls