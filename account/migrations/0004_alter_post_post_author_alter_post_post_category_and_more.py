# Generated by Django 4.0.3 on 2022-04-04 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_category_rename_tag_profile_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(default='auth.User', on_delete=django.db.models.deletion.PROTECT, related_name='author_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.ManyToManyField(to='account.category'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='uuser', to=settings.AUTH_USER_MODEL),
        ),
    ]