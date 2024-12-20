# Generated by Django 5.1.2 on 2024-12-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0006_remove_user_last_login_alter_user_password_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="user",
            name="phoneNumber",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
