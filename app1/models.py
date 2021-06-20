from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.

class Brand(models.Model):
    BRANd_nAME = [
            ('Samsung' , 'Samsung'),
            ('Apple' , 'Apple'),
            ('Huawei' , 'Huawei'),
            ('Oppo' , 'Oppo'),
            ('xiaomi' , 'xiaomi'),
        ]
    name = models.CharField( choices=BRANd_nAME , max_length=100 , verbose_name=_('اسم البراند'))
    def __str__(self):
        return self.name
    def get_devices_count(self):
        return Device.objects.filter(Device__Brand=self).count()


class Device(models.Model):
    #pdobjects = DataFrameManager()
    
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.PROTECT)
    modeldev = models.CharField(max_length=20, blank=True, null=True)
    NameDev = models.CharField(default=modeldev, primary_key=True , max_length=120, verbose_name=_("Name"))
    DisplayTypeDev = models.CharField(max_length=200, verbose_name=_("Screen Type"), blank=True, null=True)
    DisplaySizeDev = models.CharField(max_length=200, verbose_name=_("Screen Size"), blank=True, null=True)
    def __str__(self):
        return self.NameDev