# Generated by Django 4.1.4 on 2023-01-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0004_alter_project_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="img",
            field=models.ImageField(
                blank=True, null=True, upload_to="portfolio/images/"
            ),
        ),
    ]
