# Generated by Django 4.0.1 on 2022-06-21 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookland', '0008_delete_bookseites_eng'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='reg_f_eng',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookland.register_eng'),
        ),
    ]
