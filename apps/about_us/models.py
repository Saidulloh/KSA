from django.db import models


class AboutUs(models.Model):
    """
    Model for information about us
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    content = models.CharField(
        max_length=256,
        verbose_name='content'
    )
    desctiption = models.TextField(
        verbose_name='description'
    )

    def __str__(self) -> str:
        return f'{self.id} -- {self.title}'
    
    class Meta:
        verbose_name = 'about us information'
        verbose_name_plural = 'About us informations'
