# Generated by Django 3.1 on 2022-03-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionaire',
            name='if_no_why',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
