# System
import os
from dotenv import load_dotenv


load_dotenv()


class SERVICE:
    """
    Service Config
    """

    DJANGO_SETTINGS_MODULE = os.getenv("DJANGO_SETTINGS_MODULE")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = bool(int(os.getenv("DEBUG", False)))
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")


class SYSTEM_CODE:
    """
    각종 System Code
    """

    # 0 Success
    SUCCESS = ("0000", "success")

    # 9000 ~ 9999 Custom Error
    BAD_REQUEST = ("9999", "잘못된 요청입니다.")
    UNKNOWN_SERVER_ERROR = ("9999", "UNKNOWN_SERVER_ERROR")
    CLIENT_ERROR = ("9999", "CLIENT_ERROR")

    INVALID_FORMAT_COMMON = ("9999", "요청 형식이 올바르지 않습니다.")


class AWS:
    """
    AWS Confige
    """

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
