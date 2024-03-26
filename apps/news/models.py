from django.db import models


class New(models.Model):
    """
    Model for news
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='created_at'
    )
    image = models.ImageField(
        upload_to='news_images/',
        verbose_name='image'
    )
    content = models.TextField(
        verbose_name='content'
    )
    description = models.TextField(
        verbose_name='description'
    )
    second_image = models.ImageField(
        upload_to='news_second_images/',
        verbose_name='second_image'
    )
    third_image = models.ImageField(
        upload_to='news_third_images/',
        verbose_name='third_image'
    )
    second_content = models.CharField(
        max_length=256,
        verbose_name='second_content'
    )
    third_content = models.CharField(
        max_length=256,
        verbose_name='third_content'
    )
    fourth_content = models.CharField(
        max_length=256,
        verbose_name='fourth_content'
    )
    fifth_content = models.CharField(
        max_length=256,
        verbose_name='fifth_content'
    )
    sixth_content = models.CharField(
        max_length=256,
        verbose_name='sixth_content'
    )

    def __str__(self) -> str:
        return f'{self.id} -- {self.title}'
    
    class Meta:
        verbose_name = 'new'
        verbose_name_plural = 'News'
