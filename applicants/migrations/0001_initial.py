# Generated by Django 5.1.7 on 2025-03-20 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('school', models.CharField(max_length=200)),
                ('program', models.ManyToManyField(to='programs.program')),
                ('subjects', models.ManyToManyField(to='subjects.grade')),
            ],
        ),
    ]
