# Generated by Django 3.0.7 on 2020-06-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='id',
        ),
        migrations.AlterField(
            model_name='stock',
            name='ticker',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
