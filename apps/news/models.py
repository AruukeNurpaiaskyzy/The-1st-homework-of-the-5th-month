from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=155, verbose_name = "заголовка")
    description = models.TextField(verbose_name= "описание")
def __str__(self):
    return self.title
class Meta:
    verbose_name = ""
    verbose_name_plural = "основные настройки"