# Generated by Django 3.2.8 on 2021-11-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20211107_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='criado_por',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
