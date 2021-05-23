# Generated by Django 3.1.7 on 2021-05-23 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speialists', models.CharField(choices=[('جلدية', 'جلدية'), ('اسنان', 'اسنان'), ('نفسي', 'نفسي'), ('اطفال حديثي الولادة', 'اطفال حديثي الولادة'), ('مخ واعصاب', 'مخ واعصاب'), ('عظام', 'عظام'), ('نساء وتوليد', 'نساء وتوليد'), ('انف واذن وحنجرة', 'انف واذن وحنجرة'), ('قلب واوعية دموية', 'قلب واوعية دموية'), ('امراض دم', 'امراض دم'), ('اورام', 'اورام'), ('باطنه', 'باطنه'), ('تخسيس وتغذية', 'تخسيس وتغذية'), ('جراحة اطفال', 'جراحة اطفال'), ('جراحة اورام', 'جراحة اورام'), ('جراحة اوعية دموية', 'جراحة اوعية دموية'), ('جراحة تجميل', 'جراحة تجميل'), ('جراحه سمنة ومناظير', 'جراحه سمنة ومناظير')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='doctor_profile_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=5)),
                ('desription', models.TextField(blank=True, max_length=5000, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('waiting_time', models.FloatField(blank=True, max_length=5, null=True)),
                ('opening_hours', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('doctor_image', models.ImageField(upload_to='doctor_photo/')),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'place',
                'verbose_name_plural': 'places',
            },
        ),
        migrations.CreateModel(
            name='subscribed_mails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='rate_doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_value', models.FloatField(default=0.0)),
                ('date_rate', models.DateField()),
                ('time_rate', models.TimeField()),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_name', to='index.doctor_profile_1')),
                ('user_rate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='doctor_reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('date_reservation1', models.DateField()),
                ('time_reservation', models.TimeField()),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_doctor', to='index.doctor_profile_1')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='doctor_profile_1',
            name='address1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_place', to='index.place'),
        ),
        migrations.AddField(
            model_name='doctor_profile_1',
            name='specialist_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_category', to='index.category'),
        ),
        migrations.AddField(
            model_name='doctor_profile_1',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
