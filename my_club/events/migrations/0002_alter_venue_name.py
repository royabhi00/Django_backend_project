# Generated by Django 3.2 on 2022-01-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Venue Name'),
        ),
    ]