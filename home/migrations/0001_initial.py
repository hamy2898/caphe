# Generated by Django 2.2.4 on 2019-11-25 10:17

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cus_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='BaiViet',
            fields=[
                ('baiviet_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('tieude', models.CharField(max_length=300)),
                ('noidung', models.TextField()),
                ('ngay_dang', models.DateTimeField(default=django.utils.timezone.now)),
                ('anhbia', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.FloatField()),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('note', models.TextField()),
                ('payment_status', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('accept', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField(default='')),
                ('product_img', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('sale_price', models.IntegerField(default=0)),
                ('investory', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('pro_price', models.IntegerField()),
                ('pro_image', models.CharField(default='', max_length=255)),
                ('quantity', models.IntegerField()),
                ('status', models.SmallIntegerField(blank=True, null=True)),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Order')),
                ('pro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Product')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('ordered_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ordered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='home.CartItem')),
            ],
        ),
    ]
