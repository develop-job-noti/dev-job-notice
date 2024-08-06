# Generated by Django 5.0.4 on 2024-08-06 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
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
                        verbose_name="유저 고유 아이디",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="사용자 이메일 주소"
                    ),
                ),
                (
                    "nickname",
                    models.CharField(max_length=16, verbose_name="유저 닉네임"),
                ),
                ("password", models.CharField(max_length=128, verbose_name="비밀번호")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="활성 사용자 여부"),
                ),
                (
                    "is_admin",
                    models.BooleanField(default=False, verbose_name="어드민 여부"),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="탈퇴 여부"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        default=None, null=True, verbose_name="탈퇴 일시"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
