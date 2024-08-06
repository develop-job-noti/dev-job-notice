from django.db import models


class BaseName(models.Model):
    name = models.CharField(max_length=16, verbose_name="이름")

    class Meta:
        abstract = True


class BaseDescription(models.Model):
    description = models.CharField(max_length=64, null=True, verbose_name="설명")

    class Meta:
        abstract = True


class TechStack(BaseName, BaseDescription):
    id = models.AutoField(primary_key=True, verbose_name="기술 스택 고유 아이디")

    class Meta:
        db_table = "tech_stack"


class DevOccupation(BaseName, BaseDescription):
    id = models.AutoField(primary_key=True, verbose_name="개발 직무 고유 아이디")

    class Meta:
        db_table = "dev_occupation"


class ExperienceYear(BaseName, BaseDescription):
    id = models.AutoField(primary_key=True, verbose_name="경력 고유 아이디")

    class Meta:
        db_table = "experience_year"


class Area(BaseName, BaseDescription):
    id = models.AutoField(primary_key=True, verbose_name="지역 고유 아이디")

    class Meta:
        db_table = "area"


class Company(BaseName):
    id = models.AutoField(primary_key=True, verbose_name="기업 고유 아이디")

    class Meta:
        db_table = "company"


class RecruitSite(BaseName):
    id = models.AutoField(primary_key=True, verbose_name="채용 사이트 고유 아이디")
    link = models.CharField(max_length=512, verbose_name="링크")

    class Meta:
        db_table = "recruit_site"
