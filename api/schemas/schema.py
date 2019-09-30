import graphene
from .task_schema import task_schema


class Query(task_schema.TaskQuery):
    pass


schema = graphene.Schema(query=Query)