# Generated by Django 2.2.9 on 2019-12-19 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='InstagramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('counterpart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='counterpart_set', to='many_to_many.InstagramUser')),
                ('me', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='me_set', to='many_to_many.InstagramUser')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('similar_products', models.ManyToManyField(related_name='_product_similar_products_+', to='many_to_many.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('clubs', models.ManyToManyField(through='many_to_many.Career', to='many_to_many.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('toppings', models.ManyToManyField(to='many_to_many.Topping')),
            ],
        ),
        migrations.AddField(
            model_name='instagramuser',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='many_to_many.Relation', to='many_to_many.InstagramUser'),
        ),
        migrations.CreateModel(
            name='FacebookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('friends', models.ManyToManyField(related_name='_facebookuser_friends_+', to='many_to_many.FacebookUser')),
            ],
        ),
        migrations.AddField(
            model_name='career',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='many_to_many.Club'),
        ),
        migrations.AddField(
            model_name='career',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='many_to_many.Player'),
        ),
    ]
