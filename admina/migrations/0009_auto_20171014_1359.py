# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('admina', '0008_auto_20170923_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImageForge',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Img', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/user')),
                ('IsUse', models.BooleanField(default=True)),
                ('UploadDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='apply',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e2d3b4-b0a4-11e7-a7d8-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e2fadc-b0a4-11e7-9b7b-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='creation',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e25e34-b0a4-11e7-a531-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='creation2projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e25e35-b0a4-11e7-b332-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='follow',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e32280-b0a4-11e7-a6e7-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='helpapplication',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e39782-b0a4-11e7-97d4-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e2d3b5-b0a4-11e7-9c23-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='praise',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e2ac82-b0a4-11e7-80f3-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e1c189-b0a4-11e7-8ea4-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='project2projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e1e8b5-b0a4-11e7-b265-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='projectlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e1e8b4-b0a4-11e7-8e0f-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e23702-b0a4-11e7-a347-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e2855c-b0a4-11e7-9d6d-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e3492e-b0a4-11e7-a6f9-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='score',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e3492f-b0a4-11e7-ba3b-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='scorechange',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e3705c-b0a4-11e7-8833-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e1c188-b0a4-11e7-88cb-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='user2userlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e20fd9-b0a4-11e7-8ea1-c85b7634aac6'), null=True),
        ),
        migrations.AlterField(
            model_name='userlabel',
            name='Uuid',
            field=models.UUIDField(blank=True, default=uuid.UUID('e1e20fd8-b0a4-11e7-b172-c85b7634aac6'), null=True),
        ),
        migrations.AddField(
            model_name='userimageforge',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserImageForge_User_set', to='admina.User'),
        ),
    ]