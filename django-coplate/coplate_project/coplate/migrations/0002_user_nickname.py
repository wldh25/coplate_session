# Generated by Django 4.2 on 2024-06-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
