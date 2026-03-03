from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories',
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='notes',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-create_at']


    def __str__(self):
        return self.title
