# Generated by Django 4.1.3 on 2023-03-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paxfu', '0002_rename_first_name_person_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=30)),
            ],
        ),
    ]
