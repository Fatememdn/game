# Generated by Django 5.1.1 on 2024-09-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottles', '0002_bottleitem_max_characters_alter_bottleitem_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottleitem',
            name='text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
