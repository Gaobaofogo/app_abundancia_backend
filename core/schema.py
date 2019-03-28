from django.contrib.auth.decorators import login_required

import graphene

from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

from .models import Task, DoneTask
from .utils import token_required


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class DoneTaskType(DjangoObjectType):
    class Meta:
        model = DoneTask


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType, id=graphene.Int())
    done_task = graphene.List(DoneTaskType)

    @token_required
    def resolve_tasks(self, info, id=None, **kwargs):
        if id:
            return Task.objects.filter(id=id)

        return Task.objects.all()

    @token_required
    def resolve_done_task(self, info, **kwargs):
        return DoneTask.objects.all()


class UploadMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, file, **kwargs):
        # do something with your file

        return UploadMutation(success=True)


class Mutation(graphene.ObjectType):
    upload_file = UploadMutation.Field()
