# Generated by Django 3.1.2 on 2020-10-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(max_length=4000),
        ),
    ]
