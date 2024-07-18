# System
import requests
from rest_framework import status
from rest_framework.authentication import BaseAuthentication

# Project
from core.exception import raise_exception
from core.constants import SYSTEM_CODE

import logging

logger = logging.getLogger("monitor")


class SecureTokenAuthentication(BaseAuthentication):
    """
    Custom Authentication
    """

    def authenticate(self, request):
        """
        Custom Authentication
        """
        secure_token = request.META.get("HTTP_$SECURE_TOKEN")

        if not secure_token:
            None

        headers = {
            "$client_type": "pc",
            "$version": "0.0.1",
            "$language": "ko",
            "$secure_token": secure_token,
        }

        response = requests.get("http://devariapp.t-ime.com/ari2022", headers=headers)
        response_data = response.json()

        if response_data.get("result_code") == "4001":
            logger.info(f"Secure Token Authentication Failed: {response_data}")
            raise_exception(status=401, code=SYSTEM_CODE.REQUIRED_LOGIN)

        return (None, secure_token)
