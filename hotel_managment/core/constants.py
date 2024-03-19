from django.db.models import TextChoices

class UserPermissionsTypes(TextChoices):
    client = "client", "client"
    functionary = "functionary", "functionary"
    admin = "admin", "admin"
