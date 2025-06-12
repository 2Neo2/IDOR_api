from typing import Optional

from rest_framework import authentication, exceptions
from rest_framework_api_key.permissions import KeyParser

from django.http import HttpRequest
from django.conf import settings

from .models import ClientAPIKey


class APIKeyAuthentication(authentication.BaseAuthentication):
    key_parser: KeyParser = KeyParser()

    def get_key(self, request: HttpRequest) -> Optional[str]:
        return self.key_parser.get(request)

    def authenticate(self, request: HttpRequest) -> Optional[tuple]:
        key: Optional[str] = self.get_key(request)

        if not key:
            return None

        try:
            api_key: ClientAPIKey = ClientAPIKey.objects.get_from_key(key)

        except ClientAPIKey.DoesNotExist:
            raise exceptions.AuthenticationFailed('Incorrect authentication credentials.')

        # if not api_key.user.is_active:
        #     raise exceptions.AuthenticationFailed('User is deactivated.')

        return api_key.client, None
