# Generated by Django 4.0.3 on 2022-05-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovnis_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='continent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]