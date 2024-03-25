from django.db import models


class Baner(models.Model):
    """
    Model for baner
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    image = models.ImageField( #сделать так что бы отображалось только последнее image
        upload_to='baner_images/',
        verbose_name='image'
    )

    def __str__(self) -> str:
        return f'{self.id} -- {self.title}'