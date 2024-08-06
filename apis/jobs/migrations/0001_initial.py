# Generated by Django 5.0.4 on 2024-08-06 23:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("filters", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobNotice",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성 일시"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정 일시"),
                ),
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        verbose_name="공고 고유 아이디",
                    ),
                ),
                (
                    "third_party_id",
                    models.IntegerField(verbose_name="타사 채용공고 아이디"),
                ),
                ("title", models.CharField(max_length=128, verbose_name="채용공고명")),
                ("url", models.CharField(max_length=512, verbose_name="채용공고 링크")),
                ("start_at", models.DateTimeField(verbose_name="시작일")),
                ("end_at", models.DateTimeField(verbose_name="마감일")),
                (
                    "area",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filters.area",
                        verbose_name="지역 고유 아이디",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filters.company",
                        verbose_name="기업 고유 아이디",
                    ),
                ),
                (
                    "dev_occupation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filters.devoccupation",
                        verbose_name="개발 직무 고유 아이디",
                    ),
                ),
                (
                    "experience_year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filters.experienceyear",
                        verbose_name="경력 고유 아이디",
                    ),
                ),
                (
                    "recruitment_site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filters.recruitsite",
                        verbose_name="채용 사이트 고유 아이디",
                    ),
                ),
                (
                    "tech_stack",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="filters.techstack",
                        verbose_name="기술 스택 고유 아이디",
                    ),
                ),
            ],
            options={
                "db_table": "job_notice",
            },
        ),
    ]
