import graphene

from graphene_django import DjangoObjectType

from .models import Task, TaskLog


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class TaskLogType(DjangoObjectType):
    class Meta:
        model = TaskLog


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType, id=graphene.Int())
    task_logs = graphene.List(TaskLogType)

    def resolve_tasks(self, info, id=None, **kwargs):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('Not logged in!')

        if id:
            return Task.objects.filter(id=id)

        return Task.objects.all()

    def resolve_task_logs(self, info, **kwargs):
        return TaskLogType.objects.all()
