# Generated by Django 2.1 on 2018-08-15 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_blogpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disorder',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='disorder',
            name='date_modified',
        ),
        migrations.AddField(
            model_name='story',
            name='disorder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Disorder'),
            preserve_default=False,
        ),
    ]
