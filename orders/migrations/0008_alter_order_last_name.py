# Generated by Django 3.2.13 on 2022-07-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20220701_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
