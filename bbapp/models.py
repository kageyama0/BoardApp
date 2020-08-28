from django.db import models
from django.utils import timezone

class PostModel(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="投稿日/時間",
    )

    def __str__(self):
        return f'pk:{self.pk} title:{self.title} created_at:{self.pub_date}'

    class Meta:
        db_table = 'post'
        ordering = ['-pub_date', '-id']

class CommentModel(models.Model):
    name = models.CharField('名前', max_length=255, default='名無し')
    text = models.TextField('コメント')
    pub_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="投稿日/時間",
    )
    target = models.ForeignKey(
        PostModel, on_delete=models.CASCADE, verbose_name='対象記事')

    def __str__(self):
        return self.text[:20]

    class Meta:
        db_table = 'comment'
