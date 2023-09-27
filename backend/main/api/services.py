from api.models import Automation, TaskLog


class AutomationServices:


    @staticmethod
    def query_all():
        return Automation.objects.all()
    
    @staticmethod
    def get(id):
        automation = Automation.objects.get(id=id)

        if automation:
            return automation
        else:
            return None
        
    @staticmethod
    def create(name, path):
        try:
            automation = Automation.objects.create(name=name, path=path)
            automation.save()
            return automation
        except:
            return None
        

class TaskLogServices:


    @staticmethod
    def query_all():
        return TaskLog.objects.all()
    
    @staticmethod
    def get(id):
        log = TaskLog.objects.get(id=id)

        if log:
            return log
        else:
            return None
        
    @staticmethod
    def create(description, success:bool, automation:Automation):
        try:
            log = TaskLog.objects.create(description=description, success=success, automation=automation)
            log.save()
            return log
        except:
            return None
