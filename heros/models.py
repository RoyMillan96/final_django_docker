from django.db import models

# Create your models here.
class SuperHeroe(models.Model):
    name_hero = models.CharField(max_length=150, null=True, blank=True)
    name_secret = models.CharField(max_length=150, null=True, blank=True)
    super_poder = models.ForeignKey('SuperPoder', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name_hero}"

    class Meta:
        verbose_name_plural = "SuperHeroes"

class SuperPoder(models.Model):
    name_poder = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f"{self.name_poder}"

    class Meta:
        verbose_name_plural = "SuperPoderes"
