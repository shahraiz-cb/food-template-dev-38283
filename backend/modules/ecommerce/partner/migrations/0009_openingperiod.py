# Generated by Django 2.2.28 on 2022-09-15 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0008_auto_20220912_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.PositiveIntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday'), (8, 'Public Holidays')], verbose_name='Weekday')),
                ('start', models.TimeField(blank=True, help_text="Leaving start and end time empty is displayed as 'Closed'", null=True, verbose_name='Start')),
                ('end', models.TimeField(blank=True, help_text="Leaving start and end time empty is displayed as 'Closed'", null=True, verbose_name='End')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opening_periods', to='partner.Partner', verbose_name='Partner')),
            ],
            options={
                'verbose_name': 'Opening period',
                'verbose_name_plural': 'Opening periods',
                'ordering': ['weekday'],
            },
        ),
    ]
