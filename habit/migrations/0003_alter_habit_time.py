# Generated by Django 5.1.1 on 2024-09-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_alter_action_name_alter_action_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(verbose_name='Время'),
        ),
    ]
