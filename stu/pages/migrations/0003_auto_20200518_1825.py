# Generated by Django 3.0.6 on 2020-05-18 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_todolist_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='label_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Others', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='status_values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='New', max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='label',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='status',
        ),
    ]
