# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_juniorscontactsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('mailing_list', models.BooleanField(default=False, help_text="If you select 'yes', we'll add you to our club mailing list. Don't worry - its easy to unsubscribe too!", verbose_name='Add to mailing list')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Phone number')),
                ('message', models.TextField(help_text='Message (comments/questions etc)', verbose_name='Message')),
                ('our_notes', models.TextField(blank=True, help_text='Any notes from the club about this enquiry')),
                ('submitted', models.DateTimeField(auto_now_add=True, verbose_name='Date submitted')),
            ],
            options={
                'ordering': ['submitted'],
            },
        ),
    ]
