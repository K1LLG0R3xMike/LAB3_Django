# Generated by Django 4.2.4 on 2023-10-18 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospi', '0002_remove_luchador_img_remove_medico_img_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Luchador',
        ),
    ]
