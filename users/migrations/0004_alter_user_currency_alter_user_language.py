# Generated by Django 5.0.7 on 2024-08-22 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_avatar_user_currency_user_gender_user_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('won', 'Korean won'), ('usd', 'Dollar')], max_length=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('kr', 'Korean'), ('en', 'English')], max_length=2, null=True),
        ),
    ]
