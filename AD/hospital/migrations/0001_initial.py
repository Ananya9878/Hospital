# Generated by Django 3.1.7 on 2021-03-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=1000)),
                ('no_of_doctors', models.IntegerField(default=0)),
                ('no_of_beds', models.IntegerField(default=0)),
            ],
        ),
    ]
