# Generated by Django 4.2.2 on 2023-06-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_address_line1_alter_user_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('P', 'Patient'), ('D', 'Doctor')], max_length=1),
        ),
    ]
