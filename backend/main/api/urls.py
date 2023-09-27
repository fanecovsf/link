from django.urls import path

from api.views import AutomationView, AutomationDetailView

urlpatterns = [
    path('automations/', AutomationView.as_view(), name='automation'),
    path('automations/<id>', AutomationDetailView.as_view(), name='automation_detail')
]
