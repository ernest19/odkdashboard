# Generated by Django 3.2.13 on 2022-07-10 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0010_auto_20220710_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionaire2',
            name='contact_of_respondent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='questionaire2',
            name='if_no_why_have_confidence_in_government_handling_risk_covid19',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
