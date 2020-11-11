# Generated by Django 3.1.3 on 2020-11-11 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloWorld',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('hello', models.CharField(max_length=10)),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'hello_world',
            },
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lat', models.IntegerField()),
                ('lng', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
