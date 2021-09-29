# Generated by Django 3.2.7 on 2021-09-16 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetailModel',
            fields=[
                ('worker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('team', models.CharField(blank=True, max_length=12)),
                ('remaining_leaves', models.IntegerField(default=30)),
            ],
        ),
    ]