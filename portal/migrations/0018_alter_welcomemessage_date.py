# Generated by Django 4.1.2 on 2022-10-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0017_welcomemessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='welcomemessage',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
