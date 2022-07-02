# Generated by Django 4.0.5 on 2022-06-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitaorcamento', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orc',
            name='status',
        ),
        migrations.RemoveField(
            model_name='orc',
            name='usuario',
        ),
        migrations.AddField(
            model_name='orc',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='orc',
            name='nome',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='orc',
            name='classificacao_hotel',
            field=models.CharField(choices=[('1', '1 estrela'), ('2', '2 estrela'), ('3', '3 estrelas'), ('4', '4 estrelas'), ('5', '5 estrelas'), ('6', 'acima de 5')], default=3, max_length=12),
        ),
        migrations.AlterField(
            model_name='orc',
            name='orcamento',
            field=models.CharField(blank=True, default='R$ ', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='orc',
            name='qtde_0_6',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orc',
            name='qtde_7_12',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orc',
            name='qtde_adultos',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orc',
            name='qtde_melhor_idade',
            field=models.IntegerField(default=0),
        ),
    ]