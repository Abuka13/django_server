# Generated by Django 4.2.5 on 2023-10-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0005_remove_postcomments_rating_postratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomments',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
