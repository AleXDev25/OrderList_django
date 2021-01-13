# Generated by Django 3.1.2 on 2021-01-13 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('order_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('N', 'New'), ('LR', 'Layout ready'), ('IP', 'In progress'), ('D', 'Done')], default='N', max_length=15)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('deadline_date', models.DateField(verbose_name='Deadline')),
                ('price', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.customer')),
            ],
        ),
    ]