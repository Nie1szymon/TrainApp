# Generated by Django 5.0.6 on 2024-05-29 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlansTrainigs',
            new_name='PlansTrainings',
        ),
        migrations.RemoveField(
            model_name='plans',
            name='highlighted',
        ),
    ]