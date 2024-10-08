# Generated by Django 5.0.7 on 2024-08-22 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_is_host_user_name_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(choices=[('won', 'Korean won'), ('usd', 'Dollar')], default='', max_length=5),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('kr', 'Korean'), ('en', 'English')], default='', max_length=2),
        ),
    ]
