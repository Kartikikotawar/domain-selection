# Generated by Django 3.2.6 on 2021-10-04 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_task_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_tasks', to='users.team'),
        ),
    ]
