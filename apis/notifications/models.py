from django.db import models

from core.models import BaseModel
from apis.users.models import User
from apis.jobs.models import JobNotice
from apis.filters.models import (
    TechStack,
    ExperienceYear,
    DevOccupation,
    RecruitSite,
    Area,
)


class NotificationSetting(BaseModel):
    id = models.AutoField(primary_key=True, verbose_name="알림 설정 고유 아이디")
    send_at = models.DateTimeField(
        null=True, default=None, verbose_name="알림 방송 시간"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        # related_name="notification_settings",
        verbose_name="유저 고유 아이디",
    )
    tech_stack = models.ForeignKey(
        TechStack,
        on_delete=models.DO_NOTHING,
        verbose_name="기술 스택 고유 아이디",
    )
    dev_occupation = models.ForeignKey(
        DevOccupation,
        on_delete=models.DO_NOTHING,
        verbose_name="개발 직무 고유 아이디",
    )
    experience_year = models.ForeignKey(
        ExperienceYear,
        on_delete=models.DO_NOTHING,
        verbose_name="경력 고유 아이디",
    )
    recruitment_site = models.ForeignKey(
        RecruitSite,
        on_delete=models.DO_NOTHING,
        verbose_name="채용 사이트 고유 아이디",
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.DO_NOTHING,
        verbose_name="지역 고유 아이디",
    )

    class Meta:
        db_table = "notification_setting"


class Notification(BaseModel):
    id = models.AutoField(primary_key=True, verbose_name="알림 고유 아이디")

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        # related_name="notifications",
        verbose_name="유저 고유 아이디",
    )

    notification_setting = models.ForeignKey(
        NotificationSetting,
        on_delete=models.DO_NOTHING,
        # related_name="notifications",
        verbose_name="알림 설정 고유 아이디",
    )

    class Meta:
        db_table = "notification"


class NotificationType(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="알림 유형 고유 아이디")
    name = models.CharField(max_length=16, verbose_name="이름")
    description = models.CharField(max_length=64, null=True, verbose_name="설명")

    class Meta:
        db_table = "notification_type"


class NotificationJobNotice(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="알림 채용 공고 고유 아이디")
    notification = models.ForeignKey(
        Notification,
        on_delete=models.DO_NOTHING,
        # related_name="notification_job_notice",
        verbose_name="알림 고유 아이디",
    )
    job_notice = models.ForeignKey(
        JobNotice,
        on_delete=models.DO_NOTHING,
        verbose_name="공고 고유 아이디",
    )

    class Meta:
        db_table = "notification_job_notice"
