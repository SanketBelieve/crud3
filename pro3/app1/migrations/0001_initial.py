# Generated by Django 5.0.6 on 2024-07-02 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('std', models.CharField(max_length=10)),
                ('grade', models.CharField(max_length=5)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
