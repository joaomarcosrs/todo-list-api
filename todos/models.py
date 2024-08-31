from django.db import models

from accounts.models import CustomUser

class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=400)
    owner = models.ForeignKey(CustomUser, related_name='todos', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
