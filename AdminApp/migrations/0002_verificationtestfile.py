# Generated by Django 4.2.20 on 2025-04-10 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificationTestFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='verification_tests/')),
                ('filename', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='active', max_length=20)),
            ],
        ),
    ]
