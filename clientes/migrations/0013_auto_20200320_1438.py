# Generated by Django 3.0.4 on 2020-03-20 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0012_auto_20200319_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'permissions': (('alter_salary', 'Usuário pode alterar valor salario'), ('manager_dashboard-clients', 'Can view clients manager dashboar'), ('view_list', 'Can view lists'), ('view_teste', 'Can Teste'))},
        ),
    ]
