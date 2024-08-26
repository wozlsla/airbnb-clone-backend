from django.contrib import admin
from .models import Whishlist


@admin.register(Whishlist)
class WishlistAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "user",
        "created_at",
        "updated_at",
    )
