# Generated by Django 3.2.16 on 2022-10-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_messageenvoi_indicatif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageenvoi',
            name='indicatif',
            field=models.CharField(default='228', max_length=4, null=True),
        ),
    ]
