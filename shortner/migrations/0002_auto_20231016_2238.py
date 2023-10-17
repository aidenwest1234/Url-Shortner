# Generated by Django 3.2.12 on 2023-10-16 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=10000)),
                ('uuid', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Urls',
        ),
    ]
