from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import RegisterAPIView, password_change_view, password_reset_view1


urlpatterns = [
    path('create/', RegisterAPIView.as_view(), name="register"),
    path('password-change/', password_change_view, name="password_change"),
    path('password-send-check/', password_reset_view1, name="password_reset")

]


