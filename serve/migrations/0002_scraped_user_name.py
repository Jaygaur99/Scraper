# Generated by Django 3.2.5 on 2021-07-30 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serve', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scraped',
            name='user_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
