# Generated by Django 5.1.1 on 2024-10-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("past_chess", "0005_alter_game_tag_pairs"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="black_moves_comments",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name="game",
            name="white_moves_comments",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
