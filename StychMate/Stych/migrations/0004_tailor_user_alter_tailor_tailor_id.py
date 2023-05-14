# Generated by Django 4.2.1 on 2023-05-14 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Stych', '0003_remove_tailor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tailor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tailor',
            name='tailor_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]