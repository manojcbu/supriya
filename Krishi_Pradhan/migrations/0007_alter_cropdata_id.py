# Generated by Django 5.0.dev20230916185426 on 2024-05-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Krishi_Pradhan', '0006_cropdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropdata',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]