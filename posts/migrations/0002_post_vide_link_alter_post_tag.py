# Generated by Django 4.1.2 on 2022-10-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post", name="vide_link", field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="tag",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
