# Generated by Django 2.0.9 on 2018-10-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nie_hub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
