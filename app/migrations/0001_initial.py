# Generated by Django 5.0.7 on 2024-07-17 00:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/image')),
                ('music', models.FileField(upload_to='media/music')),
                ('video', models.FileField(upload_to='media/video')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descrption', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.media')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.person')),
            ],
        ),
    ]
