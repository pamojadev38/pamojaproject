# Generated by Django 4.0.4 on 2022-07-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
