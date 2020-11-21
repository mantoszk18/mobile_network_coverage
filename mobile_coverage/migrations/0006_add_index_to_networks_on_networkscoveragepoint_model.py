# Generated by Django 3.1.3 on 2020-11-21 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_coverage', '0005_change_Location_fields_to_accepting_NULL'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkcoveragepoint',
            name='networks',
            field=models.ManyToManyField(db_index=True, related_name='points', to='mobile_coverage.NetworkType'),
        ),
    ]