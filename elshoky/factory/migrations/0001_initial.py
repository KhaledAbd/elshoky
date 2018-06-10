# Generated by Django 2.0.5 on 2018-05-15 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_machine', models.CharField(choices=[('Sm', 'Shima Seiki Computrized'), ('Sc', 'Scheller Brand Tricot '), ('St', 'STOLL ANVH BLM '), ('Kn', 'Knitting Machine'), ('Em', 'embroidery')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_maker', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('salary', models.IntegerField(max_length=4)),
                ('telephone', models.IntegerField(max_length=10)),
                ('position', models.CharField(choices=[('T', 'tailor'), ('E', 'engineer'), ('C', 'cutter')], max_length=1)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Raw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_trade', models.CharField(max_length=30)),
                ('raw', models.ManyToManyField(choices=[('A', 'alpha'), ('S', 'Asher Ramadan'), ('M', 'Masrien'), ('G', 'Gawada')], to='factory.Machine')),
            ],
        ),
        migrations.AddField(
            model_name='machine',
            name='maker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.Maker'),
        ),
    ]
