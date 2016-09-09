from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from tinymce import models as tinymce_model
from embed_video.fields import EmbedVideoField
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):

        if not email:
            raise ValueError('Email is required.')

        user = self.model(
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        u"""Create superuser."""
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class ExtUser(AbstractBaseUser, PermissionsMixin):

    login = models.CharField(
        'Login',
        max_length=255,
        db_index=True
    )
    email = models.EmailField(
        'Email',
        max_length=255,
        unique=True,
        db_index=True
    )
    avatar = models.ImageField(
        'Avatar image',
        blank=True,
        null=True,
        upload_to="images/",
    )
    firstname = models.CharField(
        'First name',
        max_length=40,
        null=True,
        blank=True
    )
    lastname = models.CharField(
        'Last name',
        max_length=40,
        null=True,
        blank=True
    )
    middlename = models.CharField(
        'Middle name',
        max_length=40,
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        'Date of birth',
        null=True,
        blank=True
    )
    register_date = models.DateField(
        'Registration date',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        'Active',  # Not blocked, banned, etc
        default=True
    )
    is_admin = models.BooleanField(
        'Is superuser',
        default=False
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон"
    )
    foto = models.ImageField(
        null=True,
        blank=True,
        upload_to="images/",
        verbose_name="Фотография риелтора"
    )
    video = EmbedVideoField(
        null=True,
        blank=True,
        verbose_name="Персональное видео автора"
    )
    about = models.TextField(
        null=True,
        blank=True,
        verbose_name="Об авторе"
    )

    def __str__(self):
        return self.login

    def bit(self):
        if self.foto:
            return u'<img src="%s" width="50px">' % self.foto.url
        else:
            return "Нет изображения"

    bit.short_desription = "Фотография"
    bit.allow_tags = True

    # Django require define this method
    def get_full_name(self):
        return self.email

    @property
    def is_staff(self):
        # Required Django for admin panel
        return self.is_admin

    def get_short_name(self):
        u"""Return short name."""
        return self.email

    def __str__(self):
        u"""String representation of model. Email by default."""
        return self.email

    # Field, used as 'username' in authentication and orher forms
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Link model and model manager
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'extuser'