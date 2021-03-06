# Generated by Django 2.1.4 on 2019-01-05 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tyOfAb', models.CharField(max_length=25)),
                ('descrip', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('DOB', models.DateField(verbose_name='date of birth')),
                ('address', models.CharField(max_length=250)),
                ('genger', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='complains',
            name='u',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User'),
        ),
    ]
