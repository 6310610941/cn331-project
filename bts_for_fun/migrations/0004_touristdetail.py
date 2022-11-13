# Generated by Django 4.1 on 2022-11-11 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bts_for_fun', '0003_tourist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Touristdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_pic', models.ImageField(blank=True, upload_to='static/touristpic/')),
                ('t_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_details', to='bts_for_fun.tourist')),
            ],
        ),
    ]
