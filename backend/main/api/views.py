from rest_framework.views import APIView, status
from rest_framework.response import Response

from api.services import AutomationServices, TaskLogServices
from api.serializers import AutomationSerializer, TaskLogSerializer


class AutomationView(APIView):


    def get(self, request):
        automations = AutomationServices.query_all()
        serializer = AutomationSerializer(automations, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        
        if data:
            serializer = AutomationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'error':'missing data'}, status=status.HTTP_400_BAD_REQUEST)
        

class AutomationDetailView(APIView):


    def get(self, request, id):
        try:
            automation = AutomationServices.get(id)
        except:
            return Response(data={'error':'automation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if automation:
            serializer = AutomationSerializer(automation)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, id):     
        try:
            automation = AutomationServices.get(id)
        except:
            return Response(data={'error':'automation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if automation:
            serializer = AutomationSerializer(automation, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, id):
        try:
            automation = AutomationServices.get(id)
        except:
            return Response(data={'error':'automation not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if automation:
            automation.delete()
            return Response(data={'deletion':'automation deleted'}, status=status.HTTP_204_NO_CONTENT)
        
