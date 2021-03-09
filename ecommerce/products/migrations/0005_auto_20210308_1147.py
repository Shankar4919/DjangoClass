# Generated by Django 3.1.6 on 2021-03-08 06:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(9)]),
        ),
    ]