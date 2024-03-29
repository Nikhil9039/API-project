# Generated by Django 4.2 on 2023-04-28 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.CharField(max_length=100)),
                ('schedule', models.DateTimeField()),
                ('description', models.CharField(max_length=300)),
                ('files', models.FileField(upload_to='')),
                ('moderator', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('sub_category', models.CharField(max_length=100)),
                ('rigor_rank', models.IntegerField()),
                ('attendees', models.CharField(max_length=100)),
            ],
        ),
    ]
