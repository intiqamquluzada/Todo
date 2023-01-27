# Generated by Django 3.2 on 2023-01-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todo', '0002_delete_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('deadline', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
