# Generated by Django 4.2.1 on 2023-05-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stych', '0014_alter_tailor_sku_units_worked'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='assigned_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]