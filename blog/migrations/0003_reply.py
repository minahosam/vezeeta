# Generated by Django 3.1.7 on 2021-03-18 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20210316_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_time', models.TimeField(auto_now=True)),
                ('content', models.TextField(blank=True, max_length=100, null=True)),
                ('reply_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_author', to=settings.AUTH_USER_MODEL)),
                ('reply_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comments')),
            ],
        ),
    ]