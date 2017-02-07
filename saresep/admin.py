from django.contrib import admin


# Register your models here.
from saresep.models import File, Subscribe


class FileAdmin(admin.ModelAdmin):
    list_display = '__unicode__ date icon'.split()
    fields = 'name date pdf cover'.split()

    def icon(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.cover.url
        except:
            return '<p>No Cover</p>'

    icon.allow_tags = True


class SubscribeAdmin(admin.ModelAdmin):
    list_display = 'name phone_number checked'.split()
    list_per_page = 20


admin.site.register(File, FileAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
