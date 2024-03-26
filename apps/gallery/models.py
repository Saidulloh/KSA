from django.db import models


class Gallery(models.Model):
    """
    Model for images
    """
    image = models.ImageField(
        upload_to='gallery_first_images/',
        verbose_name='first_image'
    )
    second_image = models.ImageField(
        upload_to='gallery_second_images/',
        verbose_name='second_image'
    )
    third_image = models.ImageField(
        upload_to='gallery_third_images/',
        verbose_name='third_image'
    )
    fourth_image = models.ImageField(
        upload_to='gallery_fourth_images/',
        verbose_name='fourth_image'
    )
    fifth_image = models.ImageField(
        upload_to='gallery_fifth_images/',
        verbose_name='fifth_image'
    )

    def __str__(self) -> str:
        return f'{self.id}'
    
    class Meta:
        verbose_name = 'gallery image'
        verbose_name_plural = 'Gallery images'
