# Generated by Django 3.1.3 on 2020-11-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_coverage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkTypes',
            fields=[
                ('network_type', models.CharField(max_length=5, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='networkcoveragepoint',
            name='has_2g',
        ),
        migrations.RemoveField(
            model_name='networkcoveragepoint',
            name='has_3g',
        ),
        migrations.RemoveField(
            model_name='networkcoveragepoint',
            name='has_4g',
        ),
        migrations.AddField(
            model_name='networkcoveragepoint',
            name='networks',
            field=models.ManyToManyField(related_name='points', to='mobile_coverage.NetworkTypes'),
        ),
    ]