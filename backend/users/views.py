from rest_framework_simplejwt.views import TokenObtainPairView
from .seriealizers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
