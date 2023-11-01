# Generated by Django 4.2.5 on 2023-10-07 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_app', '0006_alter_postcomments_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='postcomments',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='PostRatings',
        ),
        migrations.AddField(
            model_name='commentrating',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_app.postcomments'),
        ),
        migrations.AddField(
            model_name='commentrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]