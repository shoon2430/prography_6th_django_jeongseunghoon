# Generated by Django 3.0.3 on 2020-03-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200303_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('notice', 'Notice'), ('dailylife', 'Dailylife'), ('community', 'Community'), ('qa', 'Q&A')], default='community', max_length=10),
        ),
    ]
