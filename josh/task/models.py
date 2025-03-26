from django.db import models



class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    mobile = models.CharField(max_length=15,unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=200,choices=[('urgent','Urgent'),('normal','Normal')])
    completed_at = models.DateTimeField(null=True,blank=True)
    status  = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    users = models.ManyToManyField(User, related_name='tasks')
