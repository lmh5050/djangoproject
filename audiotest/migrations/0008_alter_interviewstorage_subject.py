# Generated by Django 4.0.2 on 2022-02-07 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiotest', '0007_interviewstorage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewstorage',
            name='subject',
            field=models.CharField(default='2022년-02월-07일-10시-56분-46초', max_length=200),
        ),
    ]
