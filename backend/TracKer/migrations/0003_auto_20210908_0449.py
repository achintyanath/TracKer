# Generated by Django 3.2.7 on 2021-09-08 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TracKer', '0002_auto_20210908_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('year', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth')])),
                ('admin', models.BooleanField(default=False)),
                ('disable', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Maintainner',
        ),
    ]
