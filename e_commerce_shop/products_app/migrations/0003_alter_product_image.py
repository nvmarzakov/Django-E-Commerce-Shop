# Generated by Django 4.2.3 on 2023-08-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0002_product_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images/'),
        ),
    ]