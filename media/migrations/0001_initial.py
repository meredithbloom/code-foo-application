# Generated by Django 4.0.3 on 2022-04-13 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('media_type', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('short_name', models.CharField(blank=True, max_length=255, null=True)),
                ('long_description', models.TextField(blank=True, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('review_url', models.CharField(blank=True, max_length=255, null=True)),
                ('review_score', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, null=True)),
                ('genres', models.TextField(blank=True, null=True)),
                ('created_by', models.TextField(blank=True, null=True)),
                ('published_by', models.TextField(blank=True, null=True)),
                ('franchises', models.TextField(blank=True, null=True)),
                ('regions', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'media',
                'managed': True,
            },
        ),
    ]
