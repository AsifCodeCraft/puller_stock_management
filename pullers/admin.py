from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import (
    Puller,
    PullerImage,
    BodyParts,
    PullerCategory,
    UserProfile
)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


class PullerImageInline(admin.TabularInline):
    model = PullerImage
    extra = 1
    max_num = 6


@admin.register(BodyParts)
class BodyPartsAdmin(admin.ModelAdmin):

    list_display = (
        'body_code',
        'body_name',
        'body_size',
        'body_weight',
        'body_price',
    )

    search_fields = (
        'body_code',
        'body_name',
        'body_size',
    )


@admin.register(PullerCategory)
class PullerCategoryAdmin(admin.ModelAdmin):

    list_display = (
        'category',
        'category_name',
    )

    search_fields = (
        'category',
        'category_name',
    )


@admin.register(Puller)
class PullerAdmin(admin.ModelAdmin):

    list_display = (
        'puller_code',
        'puller_name',
        'category',
        'puller_size',
        'puller_weight',
        'puller_price',
        'created_at',
    )

    list_filter = (
        'category',
    )

    search_fields = (
        'puller_code',
        'puller_name',
        'puller_size',
    )

    filter_horizontal = (
        'body_parts',
    )

    inlines = [
        PullerImageInline
    ]