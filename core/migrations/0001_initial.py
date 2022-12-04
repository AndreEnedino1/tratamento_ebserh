# Generated by Django 3.2.16 on 2022-12-01 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tratamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.CharField(max_length=50, verbose_name='Paciente')),
                ('medicamento', models.CharField(help_text='Ex. GENTAMICINA 40MG/mL AMP/2mL', max_length=100, verbose_name='Medicamento')),
                ('data_inicio', models.DateField(verbose_name='Inicio do tratamento')),
                ('data_fim', models.DateField(verbose_name='Fim do tratamento')),
                ('quantidade_dia', models.IntegerField(blank=True, null=True, verbose_name='Quantidade por dia')),
                ('horario', models.CharField(help_text='Ex. 8/8', max_length=10, verbose_name='Horário')),
                ('status', models.CharField(choices=[('Em Tratamento', 'Em Tratamento'), ('Encerrado', 'Encerrado')], default='Em Tratamento', max_length=20)),
            ],
            options={
                'verbose_name': 'Tratamento',
                'verbose_name_plural': 'Tratamentos',
            },
        ),
    ]