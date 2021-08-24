# Generated by Django 3.2.6 on 2021-08-24 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('struct', models.JSONField(default='{"selling_price":"","buying_price":""}', verbose_name='structure')),
            ],
        ),
    ]
