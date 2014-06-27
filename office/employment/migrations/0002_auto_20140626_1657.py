# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='higher_year',
            field=models.IntegerField(verbose_name=b'Passing Year'),
        ),
        migrations.AlterField(
            model_name='education',
            name='secondary_year',
            field=models.IntegerField(verbose_name=b'Passing Year'),
        ),
        migrations.AlterField(
            model_name='education',
            name='year',
            field=models.IntegerField(verbose_name=b'Passing Year'),
        ),
    ]
