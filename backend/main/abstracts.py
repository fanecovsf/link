from django.db import models

from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework import serializers


class AbstractServices:


    model:models.Model

    @classmethod
    def query_all(cls):
        return cls.model.objects.all()
    
    @classmethod
    def get(cls, id):
        obj = cls.model.objects.get(id=id)

        if obj:
            return obj
        else:
            return None


class AbstractAPIView(APIView):


    model_service:AbstractServices
    model_serializer:serializers.ModelSerializer

    @classmethod
    def get(cls, request):
        objs = cls.model_service.query_all()
        serializer = cls.model_serializer(objs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @classmethod
    def post(cls, request):
        data = request.data

        if data:
            serializer = cls.model_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'error':'missing data'}, status=status.HTTP_400_BAD_REQUEST)
        

class AbstractDetailAPIView(APIView):


    model_service:AbstractServices
    model_serializer:serializers.ModelSerializer

    @classmethod
    def get(cls, request, id):
        try:
            obj = cls.model_service.get(id)
        except:
            return Response(data={'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if obj:
            serializer = cls.model_serializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    @classmethod
    def put(cls, request, id):
        try:
            obj = cls.model_service.get(id)
        except:
            return Response(data={'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if obj:
            serializer = cls.model_serializer(obj, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    @classmethod
    def delete(cls, request, id):
        try:
            obj = cls.model_service.get(id)
        except:
            return Response(data={'error':'not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if obj:
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

