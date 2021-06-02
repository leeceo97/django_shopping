from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    description = models.TextField()
    stuck = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = '상품'
        verbose_name_plural = '상품'