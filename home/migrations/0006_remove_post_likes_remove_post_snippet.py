# Generated by Django 4.2.5 on 2023-09-24 03:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_post_snippet_alter_post_body"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="likes",
        ),
        migrations.RemoveField(
            model_name="post",
            name="snippet",
        ),
    ]
