# Generated by Django 4.2.6 on 2023-10-26 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('LeaderID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]