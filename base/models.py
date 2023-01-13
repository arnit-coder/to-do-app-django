from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    Task_title = models.CharField(max_length=200)
    Task_description = models.TextField(null=True, blank=True)
    Task_status = (
        ('C', 'Complete'),
        ('IC', 'Incomplete'),
    )
    task_status = models.CharField(choices=Task_status, max_length=2)
    # Time_posted = models.TimeField( null=True, blank=True)

    def __str__(self):
        return self.Task_title

    class Meta:
        ordering = ['task_status']
    
