# Generated by Django 2.2.1 on 2020-02-28 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20200228_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='sl_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Contact'),
        ),
    ]