# Generated by Django 3.1.4 on 2021-01-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to='Images')),
                ('position', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('email', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=150)),
            ],
        ),
    ]
