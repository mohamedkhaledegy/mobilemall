# Generated by Django 3.2.4 on 2021-07-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20210706_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='slug_dev',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='announcedDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Announced'),
        ),
        migrations.AlterField(
            model_name='device',
            name='batteryDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Battery Type'),
        ),
        migrations.AlterField(
            model_name='device',
            name='bluetoothDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Bluetooth'),
        ),
        migrations.AlterField(
            model_name='device',
            name='buildDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Build'),
        ),
        migrations.AlterField(
            model_name='device',
            name='cPUDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='CPU'),
        ),
        migrations.AlterField(
            model_name='device',
            name='cardSlotDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Card Slot'),
        ),
        migrations.AlterField(
            model_name='device',
            name='chipsetDev',
            field=models.CharField(blank=True, max_length=550, null=True, verbose_name='Chipset'),
        ),
        migrations.AlterField(
            model_name='device',
            name='dimensionsDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Device Dimensions'),
        ),
        migrations.AlterField(
            model_name='device',
            name='displayResDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Screen Resolution'),
        ),
        migrations.AlterField(
            model_name='device',
            name='displaySizeDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Screen Size'),
        ),
        migrations.AlterField(
            model_name='device',
            name='displayTypeDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Screen Type'),
        ),
        migrations.AlterField(
            model_name='device',
            name='internalDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Device Storage'),
        ),
        migrations.AlterField(
            model_name='device',
            name='loudspeakerDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Loudspeaker'),
        ),
        migrations.AlterField(
            model_name='device',
            name='mainCameraDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Main Camera'),
        ),
        migrations.AlterField(
            model_name='device',
            name='main_camera_featuresDev',
            field=models.CharField(blank=True, max_length=550, null=True, verbose_name='Features Main Camera'),
        ),
        migrations.AlterField(
            model_name='device',
            name='main_camera_videoDev',
            field=models.CharField(blank=True, max_length=550, null=True, verbose_name='Main Camera Video'),
        ),
        migrations.AlterField(
            model_name='device',
            name='modeldev',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='nameDev',
            field=models.CharField(max_length=320, primary_key=True, serialize=False, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='device',
            name='networkDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Network'),
        ),
        migrations.AlterField(
            model_name='device',
            name='nfcDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='NFC'),
        ),
        migrations.AlterField(
            model_name='device',
            name='oSDev',
            field=models.CharField(blank=True, max_length=350, null=True, verbose_name='Android'),
        ),
        migrations.AlterField(
            model_name='device',
            name='priceDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='device',
            name='radioDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Radio'),
        ),
        migrations.AlterField(
            model_name='device',
            name='selfieCameraDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Selfie Camera'),
        ),
        migrations.AlterField(
            model_name='device',
            name='selfie_camera_videoDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Selfie Camera Video'),
        ),
        migrations.AlterField(
            model_name='device',
            name='sensorsDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Sensors'),
        ),
        migrations.AlterField(
            model_name='device',
            name='simDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Sim'),
        ),
        migrations.AlterField(
            model_name='device',
            name='statusDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='device',
            name='usbDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='USB'),
        ),
        migrations.AlterField(
            model_name='device',
            name='wightDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Device Wight'),
        ),
        migrations.AlterField(
            model_name='device',
            name='wlanDev',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='WLAN'),
        ),
    ]