# System
import traceback
from rest_framework import status
from rest_framework.exceptions import APIException

# Project
from core.constants import SYSTEM_CODE
from core.response import create_response
from core.monitor import ServerMonitor


import logging

logger = logging.getLogger("monitor")


def default_exception_handler(exc, context):
    """
    Default Exception Handler
    예상 못하지 에러는 기본적으로 핸들러로 관리합니다.
    """

    # Call REST framework's default exception handler first,
    # to get the standard error response.

    request = context.get("request")

    response = custom_exception_handler(exc, context)

    if response:
        return response

    if response is not None:
        response.data["status_code"] = response.status_code

    error_msg = traceback.format_exc()

    ServerMonitor.report_server_error(request, error_msg)

    return create_response(
        code=SYSTEM_CODE.UNKNOWN_SERVER_ERROR,
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


def custom_exception_handler(exc, context):
    """
    Custom Exception Handler
    사용자가 지정한 에러는 이 핸들러로 관리합니다.
    """
    if not isinstance(exc, APIException):
        return None

    payload = {
        "data": {},
        "status": getattr(exc, "status_code", 400),
        "msg": getattr(exc, "detail", SYSTEM_CODE.BAD_REQUEST[1]),
        "code": getattr(exc, "code", SYSTEM_CODE.BAD_REQUEST),
    }
    return create_response(**payload)


class CustomAPIException(APIException):
    """
    Custom APIException
    사용자가 지정하는 에러는 이것으로 전체적으로 관리합니다.
    """

    def __init__(self, **kwargs):
        self.status_code = kwargs.get("status", 400)
        self.code = kwargs.get("code", SYSTEM_CODE.BAD_REQUEST)
        self.detail = self.code[1] if not kwargs.get("msg") else kwargs.get("msg")


def raise_exception(**kwargs):
    raise CustomAPIException(**kwargs)
