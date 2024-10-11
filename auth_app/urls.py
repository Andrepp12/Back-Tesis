from django.urls import path
from .views import CustomTokenObtainPairView
from .views import CreateUserView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('create-user/', CreateUserView.as_view(), name='create_user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
