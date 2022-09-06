# Generated by Django 4.1 on 2022-08-31 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('inform', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freddit.thread')),
            ],
        ),
    ]