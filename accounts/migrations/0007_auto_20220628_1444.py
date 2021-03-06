# Generated by Django 3.2.13 on 2022-06-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='ref_active',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='referral_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
