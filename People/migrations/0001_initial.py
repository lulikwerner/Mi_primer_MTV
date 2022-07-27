# Generated by Django 4.0.6 on 2022-07-26 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('DOB', models.DateField(default=True)),
                ('relationship', models.CharField(max_length=300)),
            ],
        ),
    ]
