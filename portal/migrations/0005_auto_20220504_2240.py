# Generated by Django 3.1 on 2022-05-04 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20220330_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presurvey',
            old_name='collection_elevy_help_govenment',
            new_name='contact_of_respondent',
        ),
        migrations.RenameField(
            model_name='presurvey',
            old_name='ur_opinion_elevey_increase_revenue',
            new_name='dio_contact',
        ),
        migrations.AddField(
            model_name='presurvey',
            name='collection_elevy_help_government',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='presurvey',
            name='dio_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='presurvey',
            name='enough_sensitization_campaign_on_elevy',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='presurvey',
            name='entry_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='presurvey',
            name='if_no_enough_sensitization_campaign_on_elevy',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='presurvey',
            name='if_yes_enough_sensitization_campaign_on_elevy',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='presurvey',
            name='name_of_respondent',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='presurvey',
            name='platform_you_heard_on',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='presurvey',
            name='reason_elevy_affect_momo_business_opinion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='presurvey',
            name='why_dont_you_support',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='presurvey',
            name='why_wont_collection_elevy_help_govenment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
