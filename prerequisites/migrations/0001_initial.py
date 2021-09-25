# Generated by Django 3.2.5 on 2021-09-21 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string', models.CharField(max_length=64, unique=True)),
                ('hash_code', models.CharField(max_length=512, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_code', models.CharField(max_length=512, unique=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('content', models.ManyToManyField(related_name='words_document4abstract', to='prerequisites.Word')),
                ('title', models.ManyToManyField(related_name='words_document4title', to='prerequisites.Word')),
            ],
        ),
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('file_path', models.CharField(max_length=1024)),
                ('hash_code', models.CharField(max_length=512, unique=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('documents', models.ManyToManyField(to='prerequisites.Document')),
            ],
        ),
    ]