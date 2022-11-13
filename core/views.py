from core.models import BaseModel
from rest_framework import generics, serializers

class BaseCreateView(generics.ListCreateAPIView):
    model_class = BaseModel
    pagination_class = None
