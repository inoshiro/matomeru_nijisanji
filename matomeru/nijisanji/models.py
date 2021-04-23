from django.db import models

from youtube.models import Channel


class Liver(models.Model):
    name = models.CharField('名前', max_length=100)
    ruby = models.CharField('ルビ', max_length=100,
                            blank=True, null=True)
    slug = models.CharField('Slug', max_length=50)
    channel = models.ForeignKey(Channel, models.SET_NULL,
                                blank=True, null=True)
    twitter_id = models.CharField('ツイッターID', max_length=100,
                                  blank=True, null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = 'ライバー'
        verbose_name_plural = 'ライバー'

    def __str__(self):
        return self.name
