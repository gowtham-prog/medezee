# Generated by Django 3.2.2 on 2021-07-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_medicine_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='Delivery',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]