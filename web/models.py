from django.db import models

# Create your models here.


class PenulisanIlmiah(models.Model):
    nama = models.CharField(max_length=25, null=True)
    judul_PI = models.CharField(max_length=200, null=True)
    keterangan_Sidang = models.BooleanField(
        default=False, blank=True, null=True)

    def __str__(self):
        return self.nama
