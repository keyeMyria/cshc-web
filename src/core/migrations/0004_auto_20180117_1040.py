# Generated by Django 2.0.1 on 2018-01-17 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contactsubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cshcuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
