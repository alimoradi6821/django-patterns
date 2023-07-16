
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.profile import Profile
from .models.post import Post
from django.contrib.auth.models import User

class UserProfileInline(admin.StackedInline):
    model = Profile

class NewUserAdmin(UserAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
admin.site.register(Post)