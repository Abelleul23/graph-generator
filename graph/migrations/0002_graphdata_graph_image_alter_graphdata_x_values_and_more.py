# Generated by Django 4.2.13 on 2024-05-24 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphdata',
            name='graph_image',
            field=models.ImageField(blank=True, null=True, upload_to='graph_images'),
        ),
        migrations.AlterField(
            model_name='graphdata',
            name='x_values',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='graphdata',
            name='y_values',
            field=models.CharField(max_length=1000),
        ),
    ]