# Generated by Django 5.0.7 on 2024-08-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='registration',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
