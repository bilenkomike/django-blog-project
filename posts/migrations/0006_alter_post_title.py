# Generated by Django 4.1.2 on 2022-10-11 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_rename_vide0_link_post_video_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]