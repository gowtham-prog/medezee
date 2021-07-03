# Generated by Django 3.2.2 on 2021-07-02 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_remove_medicine_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='Patient',
        ),
        migrations.AddField(
            model_name='medicine',
            name='Patient',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='appointments.patient'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='test',
            name='Patient',
        ),
        migrations.AddField(
            model_name='test',
            name='Patient',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='appointments.patient'),
            preserve_default=False,
        ),
    ]
