# Generated by Django 5.0.1 on 2024-02-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee_left',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_left', models.CharField(max_length=20)),
                ('wight_left', models.CharField(max_length=20)),
                ('price_left', models.CharField(max_length=20)),
                ('image_left', models.ImageField(upload_to='products')),
            ],
        ),
        migrations.CreateModel(
            name='Coffee_right',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_right', models.CharField(max_length=20)),
                ('wight_right', models.CharField(max_length=20)),
                ('price_right', models.CharField(max_length=20)),
                ('image_right', models.ImageField(upload_to='products')),
            ],
        ),
    ]
