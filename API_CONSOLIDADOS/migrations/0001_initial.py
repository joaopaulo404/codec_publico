# Generated by Django 4.1.2 on 2022-10-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consolidados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consolidado', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'consolidados',
                'managed': False,
            },
        ),
    ]
