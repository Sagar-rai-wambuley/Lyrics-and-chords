# Generated by Django 4.1.4 on 2022-12-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Chord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html_description', models.CharField(max_length=200)),
                ('html_keyword', models.CharField(max_length=200)),
                ('title_name', models.CharField(max_length=200)),
                ('singer', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'Chord',
            },
        ),
    ]
