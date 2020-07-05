from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone

class ReadNum(models.Model):
    read_num = models.IntegerField('阅读数量', default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class ReadNumExpandMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            objects = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return objects.read_num
        except ObjectDoesNotExist:
            return 0

class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now)
    read_num = models.IntegerField('阅读数量', default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')