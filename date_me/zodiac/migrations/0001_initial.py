# Generated by Django 5.1.3 on 2024-11-13 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zodiac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Знак зодиака')),
                ('description', models.TextField(max_length=350, verbose_name='Описание знака зодиака')),
            ],
            options={
                'verbose_name': 'Знак зодиака',
                'verbose_name_plural': 'Знаки зодиака',
            },
        ),
    ]
