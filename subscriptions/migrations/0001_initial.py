# Generated by Django 4.0.4 on 2024-05-09 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='providers.provider', verbose_name='Provider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='users.user', verbose_name='User')),
            ],
        ),
        migrations.AddIndex(
            model_name='subscription',
            index=models.Index(fields=['user'], name='subscriptio_user_id_586440_idx'),
        ),
        migrations.AddIndex(
            model_name='subscription',
            index=models.Index(fields=['provider'], name='subscriptio_provide_021624_idx'),
        ),
    ]
