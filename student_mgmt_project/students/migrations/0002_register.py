# Generated by Django 5.2.4 on 2025-07-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Email', models.EmailField(max_length=200)),
                ('Password', models.CharField(max_length=120)),
            ],
        ),
    ]
