from django.db import models


class PriceCard(models.Model):
    pc_valus = models.CharField(max_length=20, verbose_name='Цена')
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.pc_valus

    class Meta:
        verbose_name = 'Цены'
        verbose_name_plural = 'Цены'


class PriceTable(models.Model):
    pt_title = models.CharField(max_length=200, verbose_name='Услуги')
    pt_old_price = models.CharField(max_length=200, verbose_name='Старая цена')
    pt_mew_price = models.CharField(max_length=200, verbose_name='Новая цена')

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'