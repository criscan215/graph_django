import graphene
import graphql_jwt
from .task_schema import task_schema
from .user_schema import user_schema


class Query(task_schema.TaskQuery, user_schema.UserQuery, graphene.ObjectType):
    pass


class Mutation(task_schema.TaskMutation, user_schema.UserMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
