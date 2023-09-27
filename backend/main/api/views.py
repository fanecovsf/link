from rest_framework.views import APIView, status
from rest_framework.response import Response

from api.services import AutomationServices, TaskLogServices
from api.serializers import AutomationSerializer, TaskLogSerializer

from main.abstracts import AbstractAPIView, AbstractDetailAPIView


class AutomationView(AbstractAPIView):
    model_service = AutomationServices
    model_serializer = AutomationSerializer

class AutomationDetailView(AbstractDetailAPIView):
    model_service = AutomationServices
    model_serializer = AutomationSerializer

class TaskLogView(AbstractAPIView):
    model_service = TaskLogServices
    model_serializer = TaskLogSerializer

class TaskLogDetailView(AbstractDetailAPIView):
    model_service = TaskLogServices
    model_serializer = TaskLogSerializer
        
