# Generated by Django 5.0.2 on 2024-08-06 13:51

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_comment_post_alter_comment_author_article_and_more'),
       # ('auth', '0011_update_proxy_permissions'),  # Corrected dependency
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]

