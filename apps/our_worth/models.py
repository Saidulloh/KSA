from django.db import models


class OurWorth(models.Model):
    """
    Model for our worths
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    icon = models.ImageField(
        upload_to='our_worth_icons',\
        verbose_name='icon'
    )
    description = models.TextField(
        verbose_name='description'
    )

    def __str__(self) -> str:
        return f'{self.id} -- {self.title}'
    
    class Meta:
        verbose_name = 'our worth'
        verbose_name_plural = 'Our worths'
