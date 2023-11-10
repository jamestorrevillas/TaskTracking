from django.db import models
from user.models import User

class Capabilities(models.Model):
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Skills = models.TextField(null=False, blank=True)
    Achievements = models.TextField(null=False, blank=True)

    def __str__(self):
        return f'Capabilities for username {self.Username}'