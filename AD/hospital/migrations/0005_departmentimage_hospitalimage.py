# Generated by Django 3.1.7 on 2021-05-05 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20210429_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='HospitalImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='hospital/')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='department/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.department')),
            ],
        ),
    ]