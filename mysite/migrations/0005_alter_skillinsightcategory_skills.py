# Generated by Django 5.1 on 2024-08-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_alter_topskilldetails_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillinsightcategory',
            name='skills',
            field=models.ManyToManyField(related_name='skills', to='mysite.skill'),
        ),
    ]
