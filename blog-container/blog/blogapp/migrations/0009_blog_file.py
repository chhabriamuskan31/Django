# Generated by Django 4.1.1 on 2022-09-18 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_remove_committee_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='file',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]