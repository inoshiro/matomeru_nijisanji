from django.db import models


class Channel(models.Model):
    cid = models.CharField('チャンネルID', max_length=50)
    name = models.CharField('チャンネル名', max_length=100)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = 'チャンネル'
        verbose_name_plural = 'チャンネル'

    def __str__(self):
        return self.name


class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    vid = models.CharField('動画ID', max_length=50)
    title = models.CharField('タイトル', max_length=100, blank=True, null=True)
    thumbnail = models.CharField(
        'サムネイル', max_length=255, blank=True, null=True)
    published_at = models.DateTimeField('投稿日時', blank=True, null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = '動画'
        verbose_name_plural = '動画'

    def __str__(self):
        return self.title


class Matome(models.Model):
    title = models.CharField('タイトル', max_length=100)
    description = models.TextField('説明', null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = 'まとめ'
        verbose_name_plural = 'まとめ'

    def __str__(self):
        return self.title


class Scene(models.Model):
    video = models.ForeignKey('Video', on_delete=models.CASCADE)
    matome = models.ForeignKey('Matome', on_delete=models.CASCADE)
    memo = models.CharField('メモ', max_length=100, null=True)
    start_at = models.IntegerField('開始時間', default=0, null=True)
    end_at = models.IntegerField('終了時間', default=0, null=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = 'シーン'
        verbose_name_plural = 'シーン'

    def __str__(self):
        return self.memo
