# Generated by Django 5.2 on 2025-04-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='budget',
            field=models.IntegerField(blank=True, default=1000, null=True),
        ),
    ]
