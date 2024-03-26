from django.db import models


class Statistic(models.Model):
    """
    Model for statistics
    """
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    content = models.CharField(
        max_length=256,
        verbose_name='content'
    )

    def __str__(self) -> str:
        return f'{self.id} -- {self.title}'
    
    class Meta:
        verbose_name = 'statistic'
        verbose_name_plural = 'Statistics'
