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


class CreateTask(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    text = graphene.String()

    class Arguments:
        title = graphene.String()
        text = graphene.String()

    def mutate(self, info, title, text):
        task = Task()
        task.title = title
        task.text = text
        task.save()

        return CreateTask(
            id=task.id,
            title=task.title,
            text=task.text
        )


class TaskMutation(graphene.ObjectType):
    create_task = CreateTask.Field()


task_schema = graphene.Schema(query=TaskQuery, mutation=TaskMutation)
