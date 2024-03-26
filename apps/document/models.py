from django.db import models


class Document(models.Model):
    """
    Model for document images
    """
    image = models.ImageField(
        upload_to='document_first_images/',
        verbose_name='document_first_image'
    )
    second_image = models.ImageField(
        upload_to='document_second_images/',
        verbose_name='document_second_image'
    )

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        verbose_name = 'document image'
        verbose_name_plural = 'Document images'
