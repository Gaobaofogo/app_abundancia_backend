import graphene

from graphene_django import DjangoObjectType

from .models import Task, DoneTask


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class DoneTaskType(DjangoObjectType):
    class Meta:
        model = DoneTask


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType, id=graphene.Int())
    task_done = graphene.List(DoneTaskType)

    def resolve_tasks(self, info, id=None, **kwargs):
        user = info.context.user

        if id:
            return Task.objects.filter(id=id)

        return Task.objects.all()

    def resolve_done_task(self, info, **kwargs):
        return DoneTask.objects.all()
