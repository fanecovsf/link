from api.models import Automation, TaskLog

from main.abstracts import AbstractServices


class AutomationServices(AbstractServices):
    model = Automation
        

class TaskLogServices(AbstractServices):
    model = TaskLog
