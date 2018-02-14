# Generated by Django 2.0.1 on 2018-02-14 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='número identificador do cliente')),
                ('nome', models.CharField(blank=True, help_text='nome', max_length=30, null=True, verbose_name='nome do cliente')),
                ('sobrenome', models.CharField(blank=True, help_text='nome', max_length=30, null=True, verbose_name='sobrenome do cliente')),
                ('tarifa', models.FloatField(help_text='tarifa cobrada para o usuário', verbose_name='tarifa')),
            ],
        ),
        migrations.CreateModel(
            name='Leitura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='data de referência')),
                ('leitura', models.FloatField(help_text='leitura para a data', verbose_name='leitura')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faturamento.Cliente', verbose_name='cliente responsável')),
            ],
        ),
    ]
