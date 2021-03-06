# Generated by Django 3.0.2 on 2020-04-09 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csvData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=200)),
                ('truth', models.CharField(max_length=200)),
                ('cube', models.CharField(max_length=200)),
                ('google', models.FloatField(max_length=200)),
                ('google_spam', models.FloatField(max_length=200)),
                ('google_not_spam', models.CharField(max_length=200)),
                ('ibm', models.CharField(max_length=200)),
                ('ibm_spam', models.FloatField(max_length=200)),
                ('ibm_not_spam', models.FloatField(max_length=200)),
            ],
        ),
    ]
