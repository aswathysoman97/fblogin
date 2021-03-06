# Generated by Django 3.1 on 2020-10-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=120)),
                ('fullname', models.CharField(max_length=120)),
                ('dob', models.CharField(max_length=120)),
                ('qualification', models.CharField(max_length=120)),
                ('profile_picture', models.ImageField(upload_to='images')),
                ('user', models.CharField(max_length=15)),
                ('uid', models.IntegerField()),
            ],
        ),
    ]
