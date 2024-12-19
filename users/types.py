import strawberry
from strawberry import auto
import strawberry.django
from . import models


@strawberry.django.type(models.User)
class UserType:
    name: auto
    email: auto
    username: auto
