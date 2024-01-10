# Generated by Django 3.2.4 on 2024-01-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alchemy', '0008_auto_20240110_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='bomb',
            name='craftable',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='bomb',
            name='dismantlable',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='bomb',
            name='game_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='decotion',
            name='craftable',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='decotion',
            name='dismantlable',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='decotion',
            name='game_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='oil',
            name='craftable',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='oil',
            name='dismantlable',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='oil',
            name='game_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='potion',
            name='craftable',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='potion',
            name='dismantlable',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='potion',
            name='game_id',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='decotion',
            name='tox_points',
            field=models.PositiveSmallIntegerField(default=70),
        ),
    ]
