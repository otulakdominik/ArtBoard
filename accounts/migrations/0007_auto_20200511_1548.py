# Generated by Django 3.0.6 on 2020-05-11 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200511_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='emial_confirmed',
            new_name='email_confirmed',
        ),
    ]
