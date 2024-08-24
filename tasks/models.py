from django.db import models
import datetime 
from django.contrib.auth.models import User
# Create your models here.



# MODELS STRUCTURE



class Member(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=300,null=True)
    u_id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name




class TaskCategoy(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Task(models.Model):
    t_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=[
        ('To-Do', 'To-Do'),
        ('In-Progress', 'In-Progress'),
        ('Done', 'Done')
    ])
    date_created = models.DateField(default=datetime.date.today)
    due_date = models.DateField()
    priority = models.CharField(max_length=100,choices=[
        ('low','Low'),
        ('medium','Medium'),
        ('high','High')
    ])
    category = models.ForeignKey(TaskCategoy, on_delete=models.CASCADE, null=True, blank=True)
    
    assigned_to = models.ForeignKey(Member, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self) -> str:
        return self.title



class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    assigned_to = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    assigned_date = models.DateField(default=datetime.date.today)




