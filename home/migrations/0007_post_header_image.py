# Generated by Django 4.2.5 on 2023-09-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_remove_post_likes_remove_post_snippet"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="header_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]