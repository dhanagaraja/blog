# Generated by Django 4.1.1 on 2022-11-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_category_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
