# System
from django.http import HttpResponse
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """
    헬스 체크를 위한 뷰
    """

    def get(self, request):
        return HttpResponse("OK", status=200)
