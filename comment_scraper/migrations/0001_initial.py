# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dynamic_scraper', '0017_added_order_to_scraped_obj_attr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=20)),
                ('user_url', models.URLField()),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('checker_runtime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic_scraper.SchedulerRuntime')),
            ],
        ),
        migrations.CreateModel(
            name='NewsWebsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('scraper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic_scraper.Scraper')),
                ('scraper_runtime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dynamic_scraper.SchedulerRuntime')),
            ],
        ),
    ]
