# System
from rest_framework.response import Response

# Project
from core.constants import SYSTEM_CODE


def create_response(**kwargs):
    """
    Custom Response
    응답 메시지는 이것으로 관리합니다.
    """

    headers = kwargs.get("headers", None)
    data = kwargs.get("data", {})
    status = kwargs.get("status", 200)
    code = kwargs.get("code", SYSTEM_CODE.SUCCESS)
    msg = kwargs.get("msg", code[1])
    payload = {
        "data": data,
        "result_message": msg,
        "result_code": code[0],
    }

    return Response(payload, headers=headers, status=status)
