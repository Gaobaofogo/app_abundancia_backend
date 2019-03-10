import graphene

from graphene_django import DjangoObjectType

from .models import Task


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType, id=graphene.Int())

    def resolve_tasks(self, info, id=None, **kwargs):
        user = info.context.user

        if user.is_anonymous:
            raise Exception('Not logged in!')

        if id:
            return Task.objects.filter(id=id)

        return Task.objects.all()
