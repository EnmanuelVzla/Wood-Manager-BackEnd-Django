# Generated by Django 3.2.7 on 2021-10-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestorLenha', '0002_auto_20211001_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='encomenda',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='encomenda',
            name='estado',
            field=models.CharField(default='new', max_length=200),
        ),
    ]
