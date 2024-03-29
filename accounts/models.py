from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.CharField( max_length=8,
        choices=(
            ('admin', 'admin'),
            ('user', 'user')
        )
    )
    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'