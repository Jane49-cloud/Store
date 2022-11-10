# Generated by Django 4.1.2 on 2022-11-10 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_user'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', main.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('address1', models.CharField(max_length=60, verbose_name='Address line 1')),
                ('address2', models.CharField(blank=True, max_length=60, verbose_name='Address line 2')),
                ('zip_code', models.CharField(max_length=12, verbose_name='ZIP / Postal Code')),
                ('city', models.CharField(max_length=60)),
                ('country', models.CharField(choices=[('uk', 'United Kingdom'), ('us', 'United States of America'), ('Africa', 'Africa')], max_length=7)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
