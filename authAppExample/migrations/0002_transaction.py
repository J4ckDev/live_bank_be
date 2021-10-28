# Generated by Django 3.2.8 on 2021-10-28 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authAppExample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('note', models.CharField(max_length=100)),
                ('destiny_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destiny', to='authAppExample.account')),
                ('origin_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin', to='authAppExample.account')),
            ],
        ),
    ]
