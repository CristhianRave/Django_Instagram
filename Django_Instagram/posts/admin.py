from django.contrib import admin
from django.utils.html import format_html
from posts.models  import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'quote',
        'created_at',
        'image_admin',
    )

    def image_admin(self, obj):

        return format_html(
            '<img src={} width="100px height="70px" "/>', obj.image.url
            )


admin.site.register(Post, PostAdmin)