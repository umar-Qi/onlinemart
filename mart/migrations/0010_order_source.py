# Generated by Django 3.0.7 on 2020-07-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart', '0009_auto_20200629_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='source',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
