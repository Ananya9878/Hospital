# Generated by Django 3.1.7 on 2021-04-28 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20210407_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='picture',
            field=models.ImageField(default=None, upload_to='media/hospital/'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='media/department/')),
                ('description', models.CharField(max_length=1000)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
            ],
        ),
    ]
