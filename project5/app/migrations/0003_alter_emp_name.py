# Generated by Django 4.2.14 on 2024-07-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_emp_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='name',
            field=models.CharField(default='ppp', max_length=50),
            preserve_default=False,
        ),
    ]
