# Generated by Django 4.2.1 on 2023-05-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stych', '0012_alter_tailor_tailor_payout'),
    ]

    operations = [
        migrations.AddField(
            model_name='tailor',
            name='sku_units_worked',
            field=models.TextField(default='{}'),
        ),
    ]
