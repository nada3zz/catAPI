# Generated by Django 3.2 on 2021-07-12 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_alter_history_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateField(),
        ),
    ]