# Generated by Django 4.2.9 on 2024-01-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0004_auto_20240123_1554"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faqcard",
            name="position",
            field=models.PositiveIntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
