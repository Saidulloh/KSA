from django.db import models


class OurGoal(models.Model):
    """
    Model for our goals
    """
    icon = models.ImageField(
        upload_to='our_goals_images/',
        verbose_name='icon'
    )
    content = models.CharField(
        max_length=256,
        verbose_name='content'
    )

    def __str__(self) -> str:
        return f'{self.id} -- {self.content}'

    class Meta:
        verbose_name = 'our goal'
        verbose_name_plural = 'Our goals'
