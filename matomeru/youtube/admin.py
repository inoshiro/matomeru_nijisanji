from django.contrib import admin

from .models import Channel, Video, Matome, Scene


class ChannelAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


class SceneInline(admin.TabularInline):
    model = Scene
    template = "admin/youtube/scene/edit_inline/tabular.html"


class MatomeAdmin(admin.ModelAdmin):
    inlines = [
        SceneInline,
    ]


class SceneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Matome, MatomeAdmin)
admin.site.register(Scene, SceneAdmin)
