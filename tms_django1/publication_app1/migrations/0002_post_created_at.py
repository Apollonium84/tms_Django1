# Generated by Django 4.0.4 on 2022-05-02 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication_app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]