import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from core.managers import UserManager
from core.constants import UserPermissionsTypes

# Create your models here.

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    email = models.EmailField("E-mail",
                              blank=False,
                              null=False,
                              unique=True)
    level = models.CharField("Level",
                             max_length=15,
                             choices=UserPermissionsTypes,
                             blank=True,
                             null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Hotel(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    name = models.CharField("Nome",
                            max_length=255,
                            blank=False,
                            null=False)

    def __str__(self):
        return f"{self.name}"

class Room(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    number = models.PositiveIntegerField("Número do quarto",
                                         unique=True)
    beds = models.PositiveIntegerField("Quantidade de camas",
                                       null=False, blank=False)
    hotel = models.ForeignKey(Hotel,
                              on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.hotel.name} / {self.number}"

class Reservation(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    created = models.DateTimeField("Crieado em", auto_now_add=True)
    begin = models.DateTimeField()
    ends = models.DateTimeField()
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT)
    room = models.ForeignKey(Room,
                             on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user.email} / {self.room.number} / {self.created}"

