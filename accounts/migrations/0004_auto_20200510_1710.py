# Generated by Django 3.0.6 on 2020-05-10 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200510_1702'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'account', 'verbose_name_plural': 'accounts'},
        ),
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
    ]
