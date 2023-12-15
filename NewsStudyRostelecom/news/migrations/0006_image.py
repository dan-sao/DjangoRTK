# Generated by Django 4.2.6 on 2023-12-01 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(upload_to='article_images/')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.article')),
            ],
        ),
    ]
