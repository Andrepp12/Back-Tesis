from django.urls import path
from .views import CustomTokenObtainPairView
from .views import CreateUserView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('create-user/', CreateUserView.as_view(), name='create_user'),
]
