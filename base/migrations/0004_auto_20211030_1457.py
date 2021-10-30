# Generated by Django 3.2.8 on 2021-10-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_empresa_dominio'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='email_pacitente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orden',
            name='email_proficional',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orden',
            name='paciente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='empresa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='proficional',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
