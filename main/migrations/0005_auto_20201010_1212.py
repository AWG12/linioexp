# Generated by Django 3.1.1 on 2020-10-10 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200926_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallepedido',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='direccionEntrega',
        ),
        migrations.AddField(
            model_name='pedido',
            name='direccion_entrega',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_entrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pedido'),
        ),
        migrations.AlterField(
            model_name='detallepedido',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.producto'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='tarifa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
