from django.contrib import admin
from .models import Register
from .models import PressRelease
from .models import Photo
from .models import Album
from .models import Event

class AlbumAdmin(admin.ModelAdmin):
	list_display = ('title', 'date')


admin.site.register(Album, AlbumAdmin)

admin.site.register(Photo)

admin.site.register(Register)

admin.site.register(PressRelease)

admin.site.register(Event)
