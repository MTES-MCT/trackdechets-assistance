# Generated by Django 4.2.9 on 2024-01-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0006_alter_faqcard_position_alter_faqcardlink_icon_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faqcard",
            name="content",
            field=models.TextField(blank=True),
        ),
    ]
