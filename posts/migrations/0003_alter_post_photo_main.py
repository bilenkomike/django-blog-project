# Generated by Django 4.1.2 on 2022-10-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_post_vide_link_alter_post_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="photo_main",
            field=models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
        ),
    ]
