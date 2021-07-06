from django.db import models
from django.db.models.enums import Choices
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Brand(models.Model):
    brand_nAME = [
            ('Samsung' , 'Samsung'),
            ('Apple' , 'Apple'),
            ('Huawei' , 'Huawei'),
            ('Oppo' , 'Oppo'),
            ('xiaomi' , 'xiaomi'),
            ('Infinix' , 'Infinix'),
            ('Nokia' , 'Nokia'),
            ('Sony' , 'Sony'),
            ('LG' , 'LG'),
            ('HTC' , 'HTC'),
            ('Lenovo' , 'Lenovo'),
            ('Realme' , 'Realme'),
            ('Honor' , 'Honor'),
        ]
    name = models.CharField( choices=brand_nAME , max_length=100 , verbose_name=_('اسم البراند'))
    def __str__(self):
        return self.name
    def get_devices_count(self):
        return Device.objects.filter(Device__Brand=self).count()



class Device(models.Model):
    #pdobjects = DataFrameManager()
    
    slug_dev = models.SlugField(blank=True, null=True)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.PROTECT)
    modeldev = models.CharField(max_length=100, blank=True, null=True)
    nameDev = models.CharField( primary_key=True , max_length=320, verbose_name=_("Name"))
    networkDev = models.CharField(max_length=500, blank=True, null=True, verbose_name=_("Network"))
    announcedDev = models.CharField(max_length=500, blank=True, null=True, verbose_name=_("Announced"))
    statusDev = models.CharField(max_length=500, blank=True, null=True, verbose_name=_("Status"))
    dimensionsDev = models.CharField(max_length=500, verbose_name=_("Device Dimensions"), blank=True, null=True)
    wightDev = models.CharField(max_length=500, verbose_name=_("Device Wight"), blank=True, null=True)
    buildDev = models.CharField(max_length=500, verbose_name=_("Build"), blank=True, null=True)
    simDev = models.CharField(max_length=500, verbose_name=_("Sim"), blank=True, null=True)
    displayTypeDev = models.CharField(max_length=500, verbose_name=_("Screen Type"), blank=True, null=True)
    displaySizeDev = models.CharField(max_length=500, verbose_name=_("Screen Size"), blank=True, null=True)
    displayResDev = models.CharField(max_length=500, verbose_name=_("Screen Resolution"), blank=True, null=True)
    oSDev = models.CharField(max_length=350, verbose_name=_("Android"), blank=True, null=True)
    chipsetDev = models.CharField(max_length=550, verbose_name=_("Chipset"), blank=True, null=True)
    cPUDev = models.CharField(max_length=500, verbose_name=_("CPU"), blank=True, null=True)
    cardSlotDev = models.CharField(max_length=500, verbose_name=_("Card Slot"), blank=True, null=True)
    internalDev = models.CharField(max_length=500, verbose_name=_("Device Storage"), blank=True, null=True)
    mainCameraDev = models.CharField(max_length=500, verbose_name=_("Main Camera"), blank=True, null=True)
    main_camera_featuresDev = models.CharField(max_length=550, verbose_name=_("Features Main Camera"), blank=True, null=True)
    main_camera_videoDev = models.CharField(max_length=550, verbose_name=_("Main Camera Video"), blank=True, null=True)
    selfieCameraDev = models.CharField(max_length=500, verbose_name=_("Selfie Camera"), blank=True, null=True)
    selfie_camera_videoDev = models.CharField(max_length=500, verbose_name=_("Selfie Camera Video"), blank=True, null=True)
    loudspeakerDev = models.CharField(max_length=500, verbose_name=_("Loudspeaker"), blank=True, null=True)
    wlanDev = models.CharField(max_length=500, verbose_name=_("WLAN"), blank=True, null=True)
    bluetoothDev = models.CharField(max_length=500, verbose_name=_("Bluetooth"), blank=True, null=True)
    nfcDev = models.CharField(max_length=500, verbose_name=_("NFC"), blank=True, null=True)
    radioDev = models.CharField(max_length=500, verbose_name=_("Radio"), blank=True, null=True)
    usbDev = models.CharField(max_length=500, verbose_name=_("USB"), blank=True, null=True)
    sensorsDev = models.CharField(max_length=500, verbose_name=_("Sensors"), blank=True, null=True)
    batteryDev = models.CharField(max_length=500, verbose_name=_("Battery Type"), blank=True, null=True)
    priceDev = models.CharField(max_length=500, verbose_name=_("Price"), blank=True, null=True)
    imageDev = models.ImageField(upload_to='Devices/Devices_Img/', verbose_name=_("Image Device"), blank=True)
    
    def save(self , *args , **kwargs):
        if not self.slug_dev:
            self.slug_dev = slugify(self.nameDev)
        super(Device,self).save(*args, **kwargs)

    def __str__(self):
        return self.nameDev

class Spare(models.Model):
    spare_list = [
        
            ('CompScreeb' , 'CompScreeb'),
            ('Lcd' , 'Lcd'),
            ('Touch' , 'Touch'),
            ('SubBoard' , 'SubBoard'),
            ('ChargingSocket' , 'ChargingSocket'),
            ('HandfreeSocket' , 'HandfreeSocket'),
            ('Board' , 'Board'),
            ('Battery' , 'Battery'),
            ('BackCamera' , 'BackCamera'),
            ('SelfieCamera' , 'SelfieCamera'),
            ('BackGlassCover' , 'BackGlassCover'),
            ('Housing' , 'Housing'),
        ]

    spare_quality = [
        ('Original' , 'Original'),
        ('HighCopy' , 'HighCopy' ),
        ('Copy' , 'Copy'),
    ]

    slug = models.SlugField(blank=True, null=True)
    brand = models.ForeignKey(Brand,  blank=True, null=True, on_delete=models.CASCADE)
    model = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Model"))
    device_main = models.ForeignKey(Device,related_name="Device_sets", blank=True, null=True, on_delete=models.CASCADE)
    device_same = models.ManyToManyField(Device, verbose_name=_("Work For Mobiles"))
    category = models.CharField( choices=spare_list , max_length=50, blank=True, null=True)
    name = models.CharField( max_length=320, verbose_name=_("Name"))
    quality = models.CharField( choices=spare_quality , max_length=50, blank=True, null=True)
    warranty = models.IntegerField(default=0,  verbose_name=_("Warranty"))

    def __str__(self):
        return self.name
    
    def save(self , *args , **kwargs):
        if not self.slug_dev:
            self.slug_dev = slugify(self.name)
        super(Device,self).save(*args, **kwargs)
