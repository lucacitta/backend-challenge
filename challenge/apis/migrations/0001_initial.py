# Generated by Django 4.0.1 on 2022-01-11 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('auth', models.CharField(max_length=50)),
                ('https', models.BooleanField()),
                ('cors', models.BooleanField()),
                ('link', models.CharField(max_length=70)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
    ]