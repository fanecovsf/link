from django.urls import path

from api.views import AutomationView, AutomationDetailView, TaskLogView, TaskLogDetailView

urlpatterns = [
    path('automations/', AutomationView.as_view(), name='automations'),
    path('automations/<id>', AutomationDetailView.as_view(), name='automations_detail'),
    path('logs/', TaskLogView.as_view(), name='logs'),
    path('logs/<id>', TaskLogDetailView.as_view(), name='logs_detail')
]
