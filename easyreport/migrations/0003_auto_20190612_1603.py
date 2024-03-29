# Generated by Django 2.2.1 on 2019-06-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyreport', '0002_auto_20190612_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='epreuve',
            name='rc3',
            field=models.FloatField(default=None, verbose_name='3ème éprouvette'),
        ),
        migrations.AlterField(
            model_name='epreuve',
            name='rc1',
            field=models.FloatField(verbose_name='1ère éprouvette'),
        ),
        migrations.AlterField(
            model_name='epreuve',
            name='rc2',
            field=models.FloatField(verbose_name='2ème éprouvette'),
        ),
    ]
