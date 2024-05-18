# Generated by Django 4.1.3 on 2023-11-07 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0003_items_is_sold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('com_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communications', to='items.items')),
                ('members', models.ManyToManyField(related_name='communications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified_at',),
            },
        ),
        migrations.CreateModel(
            name='CommunicationMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('communication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='communication.communication')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_message', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
