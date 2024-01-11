# Generated by Django 3.2.4 on 2024-01-23 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bomb',
            fields=[
                ('baseitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='items.baseitem')),
                ('effect', models.CharField(max_length=2000)),
                ('charges', models.PositiveSmallIntegerField(default=1)),
                ('img', models.ImageField(default='assets/alchemy/default_bomb.png', null=True, upload_to='alchemy/bombs/')),
                ('duration_sec', models.PositiveIntegerField(default=5)),
            ],
            options={
                'abstract': False,
            },
            bases=('items.baseitem',),
        ),
        migrations.CreateModel(
            name='Decotion',
            fields=[
                ('baseitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='items.baseitem')),
                ('effect', models.CharField(max_length=2000)),
                ('img', models.ImageField(default='assets/alchemy/default_decotion.png', null=True, upload_to='alchemy/decotions/')),
                ('charges', models.PositiveSmallIntegerField(default=1)),
                ('duration_sec', models.PositiveIntegerField(default=1800)),
                ('tox_points', models.PositiveSmallIntegerField(default=70)),
            ],
            options={
                'abstract': False,
            },
            bases=('items.baseitem',),
        ),
        migrations.CreateModel(
            name='Oil',
            fields=[
                ('baseitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='items.baseitem')),
                ('effect', models.CharField(max_length=2000)),
                ('img', models.ImageField(default='assets/alchemy/default_oil.png', null=True, upload_to='alchemy/oils/')),
                ('charges', models.PositiveSmallIntegerField(default=30)),
                ('attack_bonus_perc', models.PositiveSmallIntegerField(default=15)),
            ],
            options={
                'abstract': False,
            },
            bases=('items.baseitem',),
        ),
        migrations.CreateModel(
            name='Potion',
            fields=[
                ('baseitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='items.baseitem')),
                ('effect', models.CharField(max_length=2000)),
                ('img', models.ImageField(default='assets/alchemy/default_potion.png', null=True, upload_to='alchemy/potions/')),
                ('charges', models.PositiveSmallIntegerField(default=3)),
                ('duration_sec', models.PositiveIntegerField(default=30)),
                ('tox_points', models.PositiveSmallIntegerField(default=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('items.baseitem',),
        ),
    ]
