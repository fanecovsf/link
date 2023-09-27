from rest_framework import serializers

from api.models import TaskLog, Automation


class AutomationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Automation
        fields = '__all__'


class TaskLogSerializer(serializers.ModelSerializer):


    class Meta:
        model = TaskLog
        fields = '__all__'
