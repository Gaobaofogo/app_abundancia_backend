import graphene

from graphene_django import DjangoObjectType

from .models import Task, TaskDone


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class TaskDone(DjangoObjectType):
    class Meta:
        model = TaskDone


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType, id=graphene.Int())
    task_done = graphene.List(TaskDone)

    def resolve_tasks(self, info, id=None, **kwargs):
        user = info.context.user

        if id:
            return Task.objects.filter(id=id)

        return Task.objects.all()

    def resolve_task_done(self, info, **kwargs):
        return TaskDone.objects.all()
