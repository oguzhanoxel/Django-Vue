# Generated by Django 3.1.4 on 2020-12-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
