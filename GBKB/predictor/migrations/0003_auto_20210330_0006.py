# Generated by Django 2.2 on 2021-03-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0002_auto_20210209_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='lift',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='location',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='lift',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='review',
            name='location',
            field=models.IntegerField(),
        ),
    ]
