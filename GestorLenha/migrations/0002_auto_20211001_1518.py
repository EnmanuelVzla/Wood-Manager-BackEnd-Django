# Generated by Django 3.2.7 on 2021-10-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestorLenha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encomenda',
            name='data_entrega',
            field=models.DateField(verbose_name='Data de Entrega'),
        ),
        migrations.AlterField(
            model_name='encomenda',
            name='estado',
            field=models.CharField(default='novo', max_length=200),
        ),
    ]
