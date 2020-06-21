from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField('类型名称', max_length=50)

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField('标题', max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    readed_num = models.IntegerField('阅读数量', default=0)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']