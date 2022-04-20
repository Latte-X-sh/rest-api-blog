# Generated by Django 4.0.3 on 2022-04-10 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.ManyToManyField(blank=True, to='account.category'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='category',
        ),
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.ManyToManyField(blank=True, to='account.category'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]