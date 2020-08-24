# Generated by Django 3.0.8 on 2020-08-22 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_delete_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=8, null=True)),
                ('address1', models.CharField(blank=True, max_length=6, null=True)),
                ('address2', models.CharField(blank=True, max_length=20, null=True)),
                ('address3', models.CharField(blank=True, max_length=20, null=True)),
                ('salon_url', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Useradviser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adviser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Adviser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='adviser',
            name='salon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Salon'),
        ),
        migrations.AddField(
            model_name='post',
            name='adviser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Adviser'),
        ),
        migrations.AddField(
            model_name='post',
            name='salon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Salon'),
        ),
    ]
