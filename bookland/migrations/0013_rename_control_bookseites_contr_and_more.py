# Generated by Django 4.0.1 on 2022-06-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookland', '0012_bookseites_content_eng_bookseites_name_eng_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookseites',
            old_name='control',
            new_name='contr',
        ),
    #     migrations.AddField(
    #         model_name='bookseites',
    #         name='content_eng',
    #         field=models.TextField(blank=True, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='bookseites',
    #         name='name_eng',
    #         field=models.CharField(blank=True, max_length=100, null=True),
    #     ),
    #     migrations.AddField(
    #         model_name='bookseites',
    #         name='name_eng1',
    #         field=models.CharField(blank=True, max_length=100, null=True),
    #     ),
    ]
