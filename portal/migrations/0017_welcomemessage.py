# Generated by Django 4.1.2 on 2022-10-26 20:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_postsurvey_reasons_for_changed_your_perception_about_the_elevy'),
    ]

    operations = [
        migrations.CreateModel(
            name='welcomeMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
