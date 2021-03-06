# Generated by Django 2.1.15 on 2020-07-09 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True,
                                         help_text='The groups this user\
                                         belongs to. A user will get\
                                         all permissions granted to each of\
                                         their groups.',
                                         related_name='user_set',
                                         related_query_name='user',
                                         to='auth.Group',
                                         verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that\
            this user has all permissions without explicitly assigning them.',
                                      verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='tag',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL
                ),
        ),
    ]
