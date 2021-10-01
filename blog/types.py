from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from blog import models


class PostType(DjangoObjectType):
    class Meta:
        model = models.Post


class CommentsType(DjangoObjectType):
    class Meta:
        model = models.Comments


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

    exclude = ('password', )
