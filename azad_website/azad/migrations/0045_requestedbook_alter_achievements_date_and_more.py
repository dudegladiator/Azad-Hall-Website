# Generated by Django 4.1.4 on 2023-12-16 16:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azad', '0044_book_alter_achievements_date_alter_event_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=20, null=True)),
                ('shelf', models.IntegerField(null=True)),
                ('studentName', models.CharField(max_length=50)),
                ('studentRoll_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='achievements',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 16, 22, 23, 9, 175818)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 22, 23, 9, 175818)),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 22, 23, 9, 175818)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 16, 22, 23, 9, 175818)),
        ),
        migrations.AlterField(
            model_name='para',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 16, 22, 23, 9, 175818)),
        ),
    ]