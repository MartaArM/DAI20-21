# Generated by Django 3.1.5 on 2021-01-10 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('miapp', '0002_auto_20201216_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
