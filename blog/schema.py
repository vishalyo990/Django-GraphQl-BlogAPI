from blog import models
import graphene
from .types import *
from .mutations import Mutation


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    posts_by_id = graphene.List(PostType, post_id=graphene.ID())

    def resolve_all_posts(root, info):
        return (
            models.Post.objects.all()
        )

    def resolve_posts_by_id(root, info, post_id):
        return (
            models.Post.objects.filter(id=post_id)
        )


schema = graphene.Schema(query=Query, mutation=Mutation)