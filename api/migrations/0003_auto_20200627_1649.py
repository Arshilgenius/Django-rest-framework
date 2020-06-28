# Generated by Django 2.2.7 on 2020-06-27 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200627_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.IntegerField()),
                ('vote_from', models.IntegerField()),
                ('quescontent', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Scrib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.IntegerField()),
                ('fromm', models.IntegerField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('scribcontent', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.IntegerField()),
                ('fromm', models.IntegerField()),
                ('vote_from', models.IntegerField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('tagcontent', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default='newuser', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]