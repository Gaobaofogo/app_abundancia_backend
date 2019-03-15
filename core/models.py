from django.conf import settings
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    video = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class TaskLog(models.Model):
    id_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return 'Id user: {} - Id task: {}'.format(self.id_user, self.id_task)
