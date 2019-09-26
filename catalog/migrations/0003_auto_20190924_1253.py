# Generated by Django 2.2.5 on 2019-09-24 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_auto_20190917_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='borrow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'On loan'), ('r', 'Reserved'), ('m', 'Maintainance'), ('a', 'Available')], default='m', help_text='Book availability', max_length=1),
        ),
    ]