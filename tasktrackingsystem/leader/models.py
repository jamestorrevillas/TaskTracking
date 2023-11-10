from django.db import models
from user.models import User
from project.models import Project

class Leader(models.Model):
    LeaderID = models.AutoField(primary_key=True, unique=True)
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return str(self)