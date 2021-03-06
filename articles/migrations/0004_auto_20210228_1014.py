# Generated by Django 3.1.6 on 2021-02-28 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0003_article_is_published"),
    ]

    operations = [
        migrations.RenameField(
            model_name="article",
            old_name="user_link",
            new_name="author",
        ),
        migrations.RemoveField(
            model_name="article",
            name="is_published",
        ),
    ]
