# Generated by Django 2.1 on 2020-06-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200621_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='readed_num',
            field=models.IntegerField(default=0, verbose_name='阅读数量'),
        ),
    ]