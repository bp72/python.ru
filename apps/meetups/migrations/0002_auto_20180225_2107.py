# Generated by Django 2.0.1 on 2018-02-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='slides_url',
            field=models.CharField(blank=True, help_text='Айфрейм можно получить iframely.com', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='video_url',
            field=models.CharField(blank=True, help_text='Лучше удалить атрибуты height и width у айфрейма', max_length=256, null=True),
        ),
    ]