# Generated by Django 2.2.9 on 2019-12-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]