from django.urls import path
from .views import (
    UserRegistrationView,
    CustomTokenObtainPairView,
    UserProfileView,
    health_check,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("healthcheck/", health_check, name="healthcheck"),
]
