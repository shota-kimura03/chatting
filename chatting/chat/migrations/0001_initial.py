# Generated by Django 3.0.5 on 2020-04-11 12:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendId', models.IntegerField()),
                ('recvId', models.IntegerField()),
                ('message', models.TextField()),
                ('sendTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]