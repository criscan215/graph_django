import graphene
from graphene_django import DjangoObjectType

from api.models import Task


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class TaskQuery(graphene.ObjectType):
    tasks = graphene.List(TaskType)

    def resolve_tasks(self, info, **kwargs):
        return Task.objects.all()


task_schema = graphene.Schema(query=TaskQuery)