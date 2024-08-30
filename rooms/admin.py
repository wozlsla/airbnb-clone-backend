from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to 0")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "rooms",
        "pet_friendly",
        "total_amenities",
        "ratings",
        "owner",
        "created_at",
        "price",
    )
    list_filter = (
        "country",
        "toilets",
        "kind",
        "amenities",
        "updated_at",
    )
    search_fields = (
        "owner__username",
        "^name",
        "=price",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
