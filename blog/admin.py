from django.contrib import admin

# Register your models here.


from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "description",
        "publish_date",
    )
    list_filter = (
        "publish_date",
    )
    list_editable = (
        "title",
        "description",
    )
    search_fields = (
         "title",
    )

    date_hierarchy = "publish_date"
    save_on_top = True

