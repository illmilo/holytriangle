# Generated by Django 5.2.3 on 2025-06-19 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExampleForm',
            new_name='ExampleModel',
        ),
        migrations.AlterModelOptions(
            name='examplemodel',
            options={},
        ),
    ]
