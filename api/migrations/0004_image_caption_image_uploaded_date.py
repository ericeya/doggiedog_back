# Generated by Django 5.0.7 on 2024-07-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_image_user_alter_image_imagesignedurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='caption',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='image',
            name='uploaded_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
