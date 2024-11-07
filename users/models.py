from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE, help_text="Введите номер телефона")
    country = models.CharField(max_length=150, verbose_name="Страна", help_text="Введите страну проживания")
    avatar = models.ImageField(upload_to="users/avatars/", **NULLABLE, help_text="Загрузите свой аватар")
    token = models.CharField(max_length=100, verbose_name="Token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("can_block_user", 'Can block users'),
        ]

    def __str__(self):
        return self.email
