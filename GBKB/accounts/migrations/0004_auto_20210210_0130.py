# Generated by Django 2.2 on 2021-02-09 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210209_2300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extentionuser',
            old_name='mobile',
            new_name='mobileNumber',
        ),
    ]