# Generated by Django 5.0.4 on 2024-08-06 23:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("filters", "0001_initial"),
        ("jobs", "0001_initial"),
        ("notifications", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
                verbose_name="유저 고유 아이디",
            ),
        ),
        migrations.AddField(
            model_name="notificationjobnotice",
            name="job_notice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="jobs.jobnotice",
                verbose_name="공고 고유 아이디",
            ),
        ),
        migrations.AddField(
            model_name="notificationjobnotice",
            name="notification",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="notifications.notification",
                verbose_name="알림 고유 아이디",
            ),
        ),
        migrations.AddField(
            model_name="notificationsetting",
            name="area",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="filters.area",
                verbose_name="지역 고유 아이디",
            ),
        ),
        migrations.AddField(
            model_name="notificationsetting",
            name="dev_occupation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="filters.devoccupation",
                verbose_name="개발 직무 고유 아이디",
            ),
        ),
        migrations.AddField(
            model_name="notificationsetting",
            name="experience_year",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="filters.experienceyear",
                verbose_name="경력 고유 아이디",
            ),
        ),
        migrations.AddField(
            model_name="notificationsetting",
            name="recruitment_site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="filters.recruitsite",
                verbose_name="채용 사이트 고유 아이디",
            ),
        ),
        migrations.AddField(
            model_name="notificationsetting",
            name="tech_stack",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="filters.techstack",
                verbose_name="기술 스택 고유 아이디",
            ),
        ),
        migrations.AddField(
            model_name="notificationsetting",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
                verbose_name="유저 고유 아이디",
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="notification_setting",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="notifications.notificationsetting",
                verbose_name="알림 설정 고유 아이디",
            ),
        ),
    ]
