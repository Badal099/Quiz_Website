# Generated by Django 4.2.2 on 2024-02-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qid',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
