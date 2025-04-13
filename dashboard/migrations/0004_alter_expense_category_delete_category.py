# Generated by Django 5.0 on 2025-04-13 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_budget_name_category_alter_expense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.budget'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
