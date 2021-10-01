import graphene
from .models import Post, Comments
from .types import *


class PostMutations(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, title, description):
        post = Post.objects.create(title=title, description=description, author=info.context.user)
        post.save()
        return PostMutations(post=post)


class UpdatePostMutations(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
        id = graphene.ID(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, id, title=None, description=None):
        post = Post.objects.get(pk=id)
        if title:
            post.title = title
        if description:
            post.description = description
        post.save()
        return UpdatePostMutations(post=post)


class CreateCommentMutations(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        post_id = graphene.ID(required=True)

    comment = graphene.Field(CommentsType)

    @classmethod
    def mutate(cls, root, info, post_id, text):
        post = Post.objects.get(id=post_id)
        comment = Comments.objects.create(post=post, text=text, author=info.context.user)
        comment.save()
        return CreateCommentMutations(comment=comment)


class DeleteCommentMutations(graphene.Mutation):
    class Arguments:

        id = graphene.ID(required=True)

    comment = graphene.Field(CommentsType)

    @classmethod
    def mutate(cls, root, info, id):
        comment = Comments.objects.get(pk=id)

        if comment:
            comment.delete()

        return DeleteCommentMutations(comment=comment)


class Mutation(graphene.ObjectType):
    create_post = PostMutations.Field()
    update_post = UpdatePostMutations.Field()
    create_comment = CreateCommentMutations.Field()
    delete_comment = DeleteCommentMutations.Field()