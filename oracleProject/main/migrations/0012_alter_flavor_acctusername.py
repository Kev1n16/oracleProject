# Generated by Django 4.1.2 on 2023-04-18 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_flavor_acctusername_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavor',
            name='acctUsername',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
