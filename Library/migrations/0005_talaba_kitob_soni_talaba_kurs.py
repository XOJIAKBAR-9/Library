# Generated by Django 5.1.1 on 2024-10-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0004_kitob_sahifa'),
    ]

    operations = [
        migrations.AddField(
            model_name='talaba',
            name='kitob_soni',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='talaba',
            name='kurs',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
