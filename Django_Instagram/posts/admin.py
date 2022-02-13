from django.contrib import admin
from django.utils.html import format_html

from posts.models import CommentPost, Post, Image

# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = (
        'user', 
        'quote', 
        'created_at', 
    )

    # def image_admin(self, obj):
    #     return format_html(
    #         ' < img src = {} width = "100px height = "70px" "/ > ', obj.image.url
    #         )


class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'author', 
        'post', 
        'created_at', 
        'comment', 
    )


admin.site.register(Post, PostAdmin)
admin.site.register(CommentPost, CommentAdmin)
