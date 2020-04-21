# Generated by Django 2.2.7 on 2020-04-17 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='ingrediente',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='receta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventarios.Receta'),
        ),
    ]
