# Generated by Django 4.0.2 on 2022-02-17 05:24

from django.db import migrations
import elearning.fields


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0002_video_text_image_file_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=elearning.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=elearning.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
