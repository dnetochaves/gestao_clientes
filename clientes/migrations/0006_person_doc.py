# Generated by Django 3.0.4 on 2020-03-16 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_docs'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='doc',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Docs'),
        ),
    ]
