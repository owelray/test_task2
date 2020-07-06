# Generated by Django 3.0.8 on 2020-07-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('amount', models.BigIntegerField()),
                ('purpose_of_payment', models.CharField(max_length=320)),
                ('status', models.IntegerField(choices=[(1, 'Created'), (2, 'On signing'), (3, 'In processing'), (4, 'Accepted'), (5, 'Paid'), (6, 'Canceled'), (7, 'Withdrawn')], default=1)),
            ],
        ),
    ]
