from django.db import models
from django.utils import timezone


# Create your models here.
class Manager(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Facility(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=25, default='Williamsburg')
    state = models.CharField(max_length=2, default='VA')
    zip = models.CharField(max_length=5, default='23185')
    phone_number = models.CharField(max_length=10)
    fax_number = models.CharField(max_length=10, blank=True)
    homepage = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    manager = models.ForeignKey(Manager, blank=True)

    def format_phone_number(self):
        if len(self.phone_number) == 10:
            return '%s.%s.%s' % (self.phone_number[0: 3],
                                 self.phone_number[3: 6],
                                 self.phone_number[6: 10])
        else:
            return self.phone_number

    class Meta:
        verbose_name_plural = 'facilities'

    def __str__(self):
        return self.name


class Item(models.Model):
    facility = models.ForeignKey(Facility)
    item_description = models.CharField(max_length=250)
    additional_information = models.CharField(max_length=250, blank=True)
    time_stamp = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.facility.name + '-' + self.facility.street_address
