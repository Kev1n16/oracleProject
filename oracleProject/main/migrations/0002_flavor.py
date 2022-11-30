# Generated by Django 3.2.15 on 2022-11-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('amt_vCPU', models.IntegerField()),
                ('amt_Memory', models.FloatField()),
                ('amt_Volume', models.FloatField()),
                ('amt_Ephemeral_Volume', models.FloatField()),
            ],
        ),
    ]
