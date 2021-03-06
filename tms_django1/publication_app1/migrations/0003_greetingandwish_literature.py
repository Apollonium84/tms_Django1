# Generated by Django 4.0.4 on 2022-05-03 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app1', '0002_post_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='GreetingAndWish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greeting', models.CharField(max_length=256)),
                ('wish', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Literature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=256)),
                ('work', models.CharField(max_length=256)),
                ('release_year', models.IntegerField()),
            ],
        ),
    ]
