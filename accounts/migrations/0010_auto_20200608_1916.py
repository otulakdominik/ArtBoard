# Generated by Django 3.0.6 on 2020-06-08 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200608_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to='Post/%Y/%m/%D/', verbose_name='picture'),
        ),
    ]
