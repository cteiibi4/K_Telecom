# Generated by Django 3.1.1 on 2020-10-04 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='code_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.typeequipment'),
        ),
    ]