# Generated by Django 2.0.2 on 2018-07-29 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('realname', models.CharField(max_length=30)),
                ('student_id', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('motivation', models.TextField()),
                ('portfolio', models.TextField()),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]