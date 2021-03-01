from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class UserAdmin(UAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = CustomUser


