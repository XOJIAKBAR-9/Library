# Generated by Django 5.1.1 on 2024-09-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_alter_kitob_options_alter_muallif_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitob',
            name='sahifa',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
