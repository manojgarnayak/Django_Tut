# Generated by Django 5.0.2 on 2024-04-03 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='id',
        ),
        migrations.AlterField(
            model_name='school',
            name='sname',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdname', models.CharField(max_length=20)),
                ('stdphno', models.CharField(max_length=20)),
                ('sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
    ]