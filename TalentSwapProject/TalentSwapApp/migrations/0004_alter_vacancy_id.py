# Generated by Django 5.0.2 on 2024-03-19 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TalentSwapApp', '0003_vacancy_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
