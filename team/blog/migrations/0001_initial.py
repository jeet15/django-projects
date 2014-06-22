# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=140)),
                ('content', models.TextField()),
                ('slug', models.BooleanField(default=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('created', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('author', models.URLField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('link_description', models.CharField(max_length=140, blank=True)),
            ],
            options={
                'ordering': [b'-created'],
            },
            bases=(models.Model,),
        ),
    ]
