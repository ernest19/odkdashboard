# Generated by Django 3.2.13 on 2022-07-10 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_questionaire2_if_no_why_think_easing_restrictions_by_president_call_right_direction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionaire2',
            old_name='if_no_why_think_easing_restrictions_by_president_call_right_direction',
            new_name='if_no_why_think_easing_restrict_by_president_call_right_direct',
        ),
    ]