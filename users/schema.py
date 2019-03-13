import graphene
import graphql_jwt

from django.contrib.auth import get_user_model

from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        exclude_fields = ('password',)


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        user = get_user_model()(
            username=username
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(graphene.ObjectType):
    users = graphene.List(UserType, id=graphene.Int())

    def resolve_users(self, info, id=None, **kwargs):
        if id:
            return get_user_model().objects.filter(id=id)

        return get_user_model().objects.all()
