from django.db import models


class Automation(models.Model):


    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    path = models.CharField(max_length=1000, blank=False, null=False)
    failed_executions = models.IntegerField(default=0)
    successfull_executions = models.IntegerField(default=0)
    total_executions = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class TaskLog(models.Model):


    description = models.CharField(max_length=5000)
    success = models.BooleanField()

    automation = models.ForeignKey(
        Automation,
        on_delete=models.CASCADE
    )
