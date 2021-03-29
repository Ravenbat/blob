# Generated by Django 3.1 on 2020-11-13 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='ownerlist',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='ownerlist',
            field=models.ManyToManyField(to='auctions.auctionlisting'),
        ),
    ]