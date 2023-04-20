# Generated by Django 3.2.18 on 2023-04-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0025_auto_20230412_1343"),
    ]

    operations = [
        migrations.AddField(
            model_name="app",
            name="brand_logo_default",
            field=models.ImageField(blank=True, null=True, upload_to="app-logos"),
        ),
        migrations.AddField(
            model_name="appinstallation",
            name="brand_logo_default",
            field=models.ImageField(
                blank=True, null=True, upload_to="app-installation-logos"
            ),
        ),
    ]
