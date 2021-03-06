# Generated by Django 3.0.5 on 2021-04-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20210414_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='audiobook',
            name='uploaded_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='uploaded_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='uploaded_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
