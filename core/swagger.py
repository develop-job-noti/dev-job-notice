# System
from drf_spectacular.utils import extend_schema, OpenApiResponse, inline_serializer
from rest_framework import serializers
from functools import wraps

# Project


def common_response_schema(status_code=200, description="성공", serializer=None):
    """
    공통 응답 스키마를 추가하는 데코레이터
    """

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            return view_func(*args, **kwargs)

        response_name = f"{serializer.__name__}Response"

        if serializer is not None and callable(serializer):
            serializer_instance = serializer()
        else:
            serializer_instance = serializers.DictField(default={})  # 기본값 설정

        response_schema = inline_serializer(
            name=response_name,
            fields={
                "data": serializer_instance,
                "result_message": serializers.CharField(default="success"),
                "result_code": serializers.CharField(default="0000"),
            },
        )

        return extend_schema(
            responses={
                status_code: OpenApiResponse(
                    description=description,
                    response=response_schema,
                )
            }
        )(view_func)

    return decorator
