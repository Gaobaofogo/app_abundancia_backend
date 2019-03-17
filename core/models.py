from django.conf import settings
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    video = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class TaskDone(models.Model):
    user = models.IntegerField()
    task = models.IntegerField()

    def __str__(self):
        return 'Id user: {} - Id task: {}'.format(self.user, self.task)
