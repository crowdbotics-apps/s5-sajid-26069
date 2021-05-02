from django.contrib import admin
from .models import Setting, Like, UserPhoto, Match, Dislike, Inbox, Profile

admin.site.register(Profile)
admin.site.register(Setting)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(UserPhoto)
admin.site.register(Match)
admin.site.register(Inbox)

# Register your models here.
