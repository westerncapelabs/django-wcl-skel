# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DummyModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msisdn', models.BigIntegerField()),
                ('product_code', models.CharField(max_length=20)),
                ('data', django_hstore.fields.DictionaryField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
