# Generated by Django 3.1.7 on 2021-10-01 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='text',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
