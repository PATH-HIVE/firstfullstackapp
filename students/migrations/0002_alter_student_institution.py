# Generated by Django 5.1.5 on 2025-02-05 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='institution',
            field=models.CharField(max_length=255),
        ),
    ]
