# Generated by Django 2.2.1 on 2020-02-28 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20200228_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number_plate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Car'),
        ),
    ]
