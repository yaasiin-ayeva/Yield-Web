# Generated by Django 3.2.13 on 2022-05-17 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='idEleve',
        ),
        migrations.AlterField(
            model_name='eleve',
            name='personne_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contacts.personne'),
        ),
    ]