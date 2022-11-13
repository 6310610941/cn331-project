# Generated by Django 4.1.1 on 2022-11-10 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bts_for_fun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stationdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt_pic', models.ImageField(blank=True, upload_to='static/stationpic/')),
                ('stt_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_details', to='bts_for_fun.station')),
            ],
        ),
    ]