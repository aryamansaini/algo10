# Generated by Django 3.1.7 on 2022-05-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20220518_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='user1',
            name='free',
            field=models.IntegerField(default=1),
        ),
    ]