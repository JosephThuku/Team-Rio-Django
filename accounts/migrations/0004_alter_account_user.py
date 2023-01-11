# Generated by Django 4.1.3 on 2022-11-29 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_user_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="account",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
