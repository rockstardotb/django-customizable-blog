from django.contrib import admin
from .models import Post, BackgroundImage, ColorPalette, FontTable, Setting
from django.utils.safestring import mark_safe

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class BackgroundImageAdmin(admin.ModelAdmin):
    def image(obj):
        return mark_safe("<a href=/images/{} target='_blank'><img src=/images/{} style='width: 50px; height:50px;'> </a>".format(obj.background_image,obj.background_image))
    def file_name(obj):
        return str(obj.background_image)[7:]


    list_display = [
                   image,
                   file_name,
                   ]

admin.site.register(BackgroundImage, BackgroundImageAdmin)

class ColorPaletteAdmin(admin.ModelAdmin):
    def name(obj):
        return obj.name
    def text_color(obj):
        return mark_safe('<b style="background-color:{}; color:{};">{}</b>'.format(obj.text_color,obj.text_color,"________"))
    def button_color(obj):
        return mark_safe('<b style="background-color:{}; color:{};">{}</b>'.format(obj.button_color,obj.button_color,"________"))
    def navbar_color(obj):
        return mark_safe('<b style="background-color:{}; color:{};">{}</b>'.format(obj.navbar_color,obj.navbar_color,"________"))
    def icon_color(obj):
        return mark_safe('<b style="background-color:{}; color:{};">{}</b>'.format(obj.icon_color,obj.icon_color,"________"))
    def container_color(obj):
        return mark_safe('<b style="background-color:{}; color:{};">{}</b>'.format(obj.container_color,obj.container_color,"________"))
    #actions = None

    list_display = [
                   name,
                   text_color,
                   button_color,
                   navbar_color,
                   icon_color,
                   container_color,
                   ]

admin.site.register(ColorPalette, ColorPaletteAdmin)

admin.site.register(FontTable)
admin.site.register(Setting)

