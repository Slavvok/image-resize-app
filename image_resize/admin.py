from django.contrib import admin
from .models import NewImage
from django.utils.safestring import mark_safe
from django.conf import settings
# Register your models here.


class NewImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'uploaded_at', '_size', '_old_size', '_image_preview']
    fields = (
        ('width', 'height'),
        ('old_width', 'old_height'),
        'image'
    )

    def _size(self, obj):
        return "%s, %s" % (obj.width, obj.height)

    def _old_size(self, obj):
        return "%s, %s" % (obj.old_width, obj.old_height)

    def _image_preview(self, obj):
        return mark_safe('<img src="{}" style="max-height: 50px" />'.format(obj.image.url))


admin.site.register(NewImage, NewImageAdmin)
