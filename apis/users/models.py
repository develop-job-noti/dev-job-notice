from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from apis.users.managers import UserManager
from core.models import BaseModel


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    """
    시스템 내 개발, 사용자를 나타내는 사용자 모델입니다.
    """

    id = models.AutoField(primary_key=True, verbose_name="유저 고유 아이디")
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name="사용자 이메일 주소",
    )
    nickname = models.CharField(max_length=16, verbose_name="유저 닉네임")
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    is_active = models.BooleanField(default=True, verbose_name="활성 사용자 여부")
    is_admin = models.BooleanField(default=False, verbose_name="어드민 여부")
    is_deleted = models.BooleanField(default=False, verbose_name="탈퇴 여부")
    deleted_at = models.DateTimeField(null=True, default=None, verbose_name="탈퇴 일시")

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        db_table = "user"

    def __str__(self) -> str:
        return self.email
