# Generated by Django 5.0.4 on 2024-06-02 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voters',
            name='Token',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
    ]