# Generated by Django 3.2 on 2021-04-30 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutapi', '0004_auto_20210429_2202'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='EventSessions',
            new_name='EventSession',
        ),
        migrations.RenameModel(
            old_name='HeadsInfo',
            new_name='HeadInfo',
        ),
        migrations.RenameModel(
            old_name='NonTechCircles',
            new_name='NonTechCircle',
        ),
        migrations.RenameModel(
            old_name='TechCircles',
            new_name='TechCircle',
        ),
        migrations.RenameModel(
            old_name='TopMembers',
            new_name='TopMember',
        ),
        migrations.AddField(
            model_name='aboutteam',
            name='body_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutteam',
            name='body_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutteam',
            name='title_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutteam',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
