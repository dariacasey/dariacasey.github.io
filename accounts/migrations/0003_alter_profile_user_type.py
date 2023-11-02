# Generated by Django 4.2.5 on 2023-09-18 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_profile_user_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="user_type",
            field=models.CharField(
                choices=[("teacher", "Teacher"), ("student", "Student")], max_length=10
            ),
        ),
    ]