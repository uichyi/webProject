# Generated by Django 5.1.6 on 2025-02-25 17:46

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestNSI',
            fields=[
                ('test_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(max_length=255)),
                ('title_all', models.CharField(max_length=255)),
                ('title_correct', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('age', models.SmallIntegerField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=255, null=True)),
                ('speciality', models.CharField(blank=True, max_length=255, null=True)),
                ('residence', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.SmallIntegerField(blank=True, null=True)),
                ('weight', models.SmallIntegerField(blank=True, null=True)),
                ('lead_hand', models.CharField(blank=True, max_length=255, null=True)),
                ('diseases', models.CharField(blank=True, max_length=255, null=True)),
                ('smoking', models.BooleanField(blank=True, null=True)),
                ('alcohol', models.CharField(blank=True, max_length=255, null=True)),
                ('sport', models.CharField(blank=True, max_length=255, null=True)),
                ('insomnia', models.BooleanField(blank=True, null=True)),
                ('current_health', models.SmallIntegerField(blank=True, null=True)),
                ('gaming', models.BooleanField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='api_user_groups', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='api_user_permissions', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('try_number', models.SmallIntegerField()),
                ('number_all_answers', models.IntegerField(blank=True, null=True)),
                ('number_correct_answers', models.IntegerField(blank=True, null=True)),
                ('complete_time', models.DurationField(blank=True, null=True)),
                ('accuracy', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.testnsi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
    ]
