# Generated by Django 5.1.1 on 2024-10-09 11:31
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("past_chess", "0003_alter_game_black_alter_game_black_moves_and_more"),
    ]

    operations = [
        HStoreExtension(),
    ]
