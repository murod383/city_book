# Generated by Django 4.2.1 on 2023-05-14 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название города')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название заведения')),
                ('description', models.TextField(null=True, verbose_name='Описание заведения')),
                ('adress', models.CharField(max_length=250, verbose_name='Адресс заведения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='city_app.category', verbose_name='Категория заведения')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='city_app.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Заведение',
                'verbose_name_plural': 'Заведения',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('additionalPhone', models.CharField(max_length=12, null=True, verbose_name='Дополнительный номер телефона')),
                ('work_routine', models.CharField(max_length=50, verbose_name='График работы')),
                ('email', models.EmailField(max_length=50, verbose_name='Почта')),
                ('image', models.ImageField(upload_to='images/')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='city_app.place')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
