# Generated by Django 2.1.3 on 2018-12-07 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ontology',
            name='authors',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Ontology',
        ),
    ]
