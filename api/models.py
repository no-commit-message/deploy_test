from django.db import models

class Post(models.Model):
    title = models.CharField("タイトル", max_length=100)
    content = models.TextField("本文")
    created_at = models.DateTimeField("投稿日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)
    skill_level = models.SmallIntegerField("スキルレベル", default=0)

    def __str__(self):
        return self.title