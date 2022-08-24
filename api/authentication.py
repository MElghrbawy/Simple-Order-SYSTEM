from rest_framework.authentication import TokenAuthentication as BaseTokenAuthentication
from rest_framework.authtoken.models import Token

class TokenAuthentication(BaseTokenAuthentication):
    keyword = 'Bearer'