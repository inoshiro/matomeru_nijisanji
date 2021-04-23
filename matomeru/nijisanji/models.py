from django.db import models


class Liver(models.Model):
    name = models.CharField('名前', max_length=100)
    twitter_id = models.CharFIeld('ツイッターID', max_length=100)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = 'ライバー'
        verbose_name_plural = 'ライバー'

    def __str__(self):
        return self.name
