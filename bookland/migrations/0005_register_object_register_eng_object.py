# Generated by Django 4.0.1 on 2022-06-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookland', '0004_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='object',
            field=models.ManyToManyField(to='bookland.Object'),
        ),
        migrations.AddField(
            model_name='register_eng',
            name='object',
            field=models.ManyToManyField(to='bookland.Object'),
        ),
    ]
