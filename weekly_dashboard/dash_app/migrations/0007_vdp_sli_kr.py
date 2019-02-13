# Generated by Django 2.1.5 on 2019-02-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash_app', '0006_delete_vdp'),
    ]

    operations = [
        migrations.CreateModel(
            name='VDP_Sli_KR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('partner_system_name', models.CharField(max_length=50)),
                ('linking_status', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
