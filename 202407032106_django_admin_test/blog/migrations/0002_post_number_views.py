# Generated by Django 5.0.6 on 2024-07-04 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number_views',
            field=models.IntegerField(null=True),
        ),
    ]
