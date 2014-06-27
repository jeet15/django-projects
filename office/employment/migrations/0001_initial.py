# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=20, verbose_name=b'First Name')),
                ('mname', models.CharField(max_length=20, verbose_name=b'Middle Name')),
                ('lname', models.CharField(max_length=20, verbose_name=b'Last Name')),
                ('city', models.CharField(max_length=50, verbose_name=b'City')),
                ('state', models.CharField(max_length=50, verbose_name=b'State')),
                ('country', models.CharField(max_length=20, verbose_name=b'Country')),
                ('pincode', models.IntegerField(default=0, verbose_name=b'Pincode')),
                ('email', models.CharField(max_length=40, verbose_name=b'Email')),
                ('mobile', models.IntegerField(default=0, verbose_name=b'Mobile Number')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employer', models.ForeignKey(to='employment.Employer', to_field='id')),
                ('higher_specification', models.CharField(max_length=20, verbose_name=b'Specification')),
                ('higher_year', models.IntegerField(default=0, verbose_name=b'Passing Year')),
                ('secondary_specification', models.CharField(max_length=20, verbose_name=b'Specification')),
                ('secondary_year', models.IntegerField(default=0, verbose_name=b'Passing Year')),
                ('graduation', models.CharField(max_length=20, verbose_name=b'Graduation')),
                ('year', models.IntegerField(default=0, verbose_name=b'Passing Year')),
                ('university', models.CharField(max_length=50, verbose_name=b'University')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
