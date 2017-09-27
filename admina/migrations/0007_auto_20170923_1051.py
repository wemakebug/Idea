# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-23 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('admina', '0006_auto_20170923_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='praise',
            name='user_prised',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Praised_User_set', to='admina.User'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f471d57c-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f472095c-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='creation',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f47175d2-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='creation2projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4718c02-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4722496-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='helpapplication',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4728490-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f471ec06-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='praise',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f471bd6c-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='praise',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Praise_User_set', to='admina.User'),
        ),
        migrations.AlterField(
            model_name='project',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f470f9e0-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='project2projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4711ed4-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4710d18-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4715f5c-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f471a642-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4723f80-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4725ace-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='scorechange',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4726ca8-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f470df96-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='user2userlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f4714ac6-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
        migrations.AlterField(
            model_name='userlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('f47133c4-a009-11e7-abc5-c03fd5f58c28'), null=True),
        ),
    ]
