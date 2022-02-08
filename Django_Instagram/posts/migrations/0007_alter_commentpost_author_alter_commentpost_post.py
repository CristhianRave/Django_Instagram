# Generated by Django 4.0.1 on 2022-02-08 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_commentpost_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpost',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentAuthor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commentpost',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='posts.post'),
        ),
    ]
