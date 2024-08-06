from django.db import models

from core.models import BaseModel
from apis.filters.models import (
    Company,
    TechStack,
    DevOccupation,
    ExperienceYear,
    Area,
    RecruitSite,
)


class JobNotice(BaseModel):
    id = models.AutoField(primary_key=True, verbose_name="공고 고유 아이디")
    third_party_id = models.IntegerField(verbose_name="타사 채용공고 아이디")
    title = models.CharField(max_length=128, verbose_name="채용공고명")
    url = models.CharField(max_length=512, verbose_name="채용공고 링크")
    start_at = models.DateTimeField(verbose_name="시작일")
    end_at = models.DateTimeField(verbose_name="마감일")

    company = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING,
        verbose_name="기업 고유 아이디",
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
        db_table = "job_notice"
