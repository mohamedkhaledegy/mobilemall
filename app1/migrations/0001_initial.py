# Generated by Django 3.2.4 on 2021-06-20 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Samsung', 'Samsung'), ('Apple', 'Apple'), ('Huawei', 'Huawei'), ('Oppo', 'Oppo'), ('xiaomi', 'xiaomi')], max_length=100, verbose_name='اسم البراند')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('modeldev', models.CharField(blank=True, max_length=20, null=True)),
                ('NameDev', models.CharField(default=models.CharField(blank=True, max_length=20, null=True), max_length=120, primary_key=True, serialize=False, verbose_name='Name')),
                ('DisplayTypeDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Screen Type')),
                ('DisplaySizeDev', models.CharField(blank=True, max_length=200, null=True, verbose_name='Screen Size')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app1.brand')),
            ],
        ),
    ]
