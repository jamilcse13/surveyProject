# Generated by Django 3.2.8 on 2022-02-20 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ['id']},
        ),
    ]