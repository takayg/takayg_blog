# Generated by Django 3.1.3 on 2020-11-24 21:32

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201125_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=markdownx.models.MarkdownxField(help_text='To Write with Markdown format', verbose_name='Contents'),
        ),
    ]