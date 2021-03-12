# Generated by Django 3.1.7 on 2021-03-01 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0005_auto_20210228_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_reservation',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
