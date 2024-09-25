# Generated by Django 5.1.1 on 2024-09-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottles', '0004_rename_bottle_bottle_bottle_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottleitem',
            name='type',
        ),
        migrations.AddField(
            model_name='bottle',
            name='read_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bottleitem',
            name='name',
            field=models.CharField(default='bottle', max_length=100),
        ),
        migrations.AlterField(
            model_name='bottleitem',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
