from django.db import models

from utils.NumberValidator import kg_phone_validator


class OurContact(models.Model):
    """
    Model for our contacts
    """ 
    email = models.EmailField(
        unique=True,
        verbose_name='email'
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[kg_phone_validator],
        verbose_name='phone_number'
    )
    address = models.CharField(
        max_length=256,
        verbose_name='address'
    )
    chart_from = models.TimeField(
        auto_now=False,
        verbose_name='chart_from'
    )
    chart_till = models.TimeField(
        auto_now=False,
        verbose_name='chart_till'
    )

    def __str__(self) -> str:
        return f'{self.id} -- {self.email}'
    
    class Meta:
        verbose_name = 'our contact'
        verbose_name_plural = 'Our contacts'
