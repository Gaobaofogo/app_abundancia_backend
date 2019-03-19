from django.conf import settings
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    video = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class DoneTask(models.Model):
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return 'User: {} - Task: {}'.format(self.user_id, self.task_id)
