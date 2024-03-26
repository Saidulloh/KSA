from django.db import models


class Industry(models.Model):
    """
    Model for industries
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    description = models.TextField(
        verbose_name='description'
    )
    image = models.ImageField(
        upload_to='industry_images/',
        verbose_name='image'
    )

    def __str__(self) -> str:
        return f'{self.id} -- {self.title}'

    class Meta:
        verbose_name = 'industry'    
        verbose_name_plural = 'Industries'
