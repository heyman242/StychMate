# Generated by Django 4.2.1 on 2023-05-14 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stych', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('hub_id', models.AutoField(primary_key=True, serialize=False)),
                ('hub_location', models.CharField(max_length=100)),
                ('hub_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_address', models.TextField()),
                ('order_status', models.CharField(default='Pending', max_length=100)),
                ('delivery_info', models.TextField()),
                ('completion_time', models.DateTimeField(blank=True, null=True)),
                ('assigned_hub', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Stych.hub')),
            ],
        ),
        migrations.CreateModel(
            name='SKU',
            fields=[
                ('sku_id', models.AutoField(primary_key=True, serialize=False)),
                ('sku_name', models.CharField(max_length=100)),
                ('sku_description', models.TextField()),
                ('sku_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='tailor',
            name='id',
        ),
        migrations.AddField(
            model_name='tailor',
            name='tailor_id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('size', models.CharField(max_length=2)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stych.order')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stych.sku')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='assigned_tailor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Stych.tailor'),
        ),
        migrations.AddField(
            model_name='order',
            name='sku',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stych.sku'),
        ),
        migrations.CreateModel(
            name='Hub_Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('size', models.CharField(max_length=2)),
                ('hub', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stych.hub')),
                ('sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stych.sku')),
            ],
        ),
    ]