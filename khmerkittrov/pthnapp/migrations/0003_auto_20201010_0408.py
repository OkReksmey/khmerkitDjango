# Generated by Django 3.1.2 on 2020-10-10 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pthnapp', '0002_auto_20201009_0333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pthn_unit',
            name='photo_credit',
        ),
        migrations.AddField(
            model_name='pthn_unit',
            name='photo_credit_thumbnail1',
            field=models.CharField(default='source?', max_length=50),
        ),
        migrations.AddField(
            model_name='pthn_unit',
            name='photo_credit_thumbnail2',
            field=models.CharField(default='source?', max_length=50),
        ),
        migrations.AddField(
            model_name='pthn_unit',
            name='photo_credit_thumbnail3',
            field=models.CharField(default='source?', max_length=50),
        ),
        migrations.AddField(
            model_name='pthn_unit',
            name='photo_credit_thumbnailIndex',
            field=models.CharField(default='source?', max_length=50),
        ),
    ]
