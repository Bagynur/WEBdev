# Generated by Django 3.0.4 on 2020-03-28 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200328_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(),
        ),
    ]
