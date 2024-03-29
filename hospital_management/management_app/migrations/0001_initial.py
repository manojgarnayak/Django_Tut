# Generated by Django 5.0.2 on 2024-03-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('sno', models.IntegerField(primary_key=True, serialize=False)),
                ('patient_details', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('disease_desc', models.CharField(max_length=150)),
            ],
        ),
    ]
