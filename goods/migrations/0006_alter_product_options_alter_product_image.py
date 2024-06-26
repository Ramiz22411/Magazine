# Generated by Django 4.2 on 2024-06-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_alter_category_name_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photo/'),
        ),
    ]
