# Generated by Django 2.2.7 on 2019-12-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191201_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, verbose_name='mobile number'),
        ),
    ]
