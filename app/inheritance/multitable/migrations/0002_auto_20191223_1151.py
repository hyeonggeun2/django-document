# Generated by Django 2.2.9 on 2019-12-23 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('multitable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='near_place',
            field=models.ManyToManyField(related_query_name='restaurant_by_near_places', to='multitable.Place'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='place_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_query_name='restaurant_by_oto', serialize=False, to='multitable.Place'),
        ),
    ]