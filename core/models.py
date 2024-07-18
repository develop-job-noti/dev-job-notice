from django.db import models


class BaseModel(models.Model):
    """
    모델의 가장 기본이 되는 BaseModel
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정시간")

    class Meta:
        abstract = True
