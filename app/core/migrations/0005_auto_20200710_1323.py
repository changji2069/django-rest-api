# Generated by Django 2.1.15 on 2020-07-10 13:23

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200710_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(
                null=True,
                upload_to=core.models.recipe_image_file_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups \
            this user belongs to. A user will get all permissions granted to\
             each of their groups.', related_name='user_set',
                                         related_query_name='user',
                                         to='auth.Group',
                                         verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(
                default=False, help_text='Designates\
             that this user has all permissions without explicitly assigning \
             them.',
                verbose_name='superuser status'),
        ),
    ]
