# Generated by Django 2.0.5 on 2018-05-18 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0004_auto_20180518_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11)),
                ('size', models.CharField(choices=[('sm', 'small'), ('ch', 'Chields'), ('M', 'medium'), ('gr', 'Girl')], max_length=2)),
                ('machine', models.ManyToManyField(to='factory.Machine')),
            ],
        ),
        migrations.RemoveField(
            model_name='models',
            name='machine',
        ),
        migrations.DeleteModel(
            name='Models',
        ),
    ]
