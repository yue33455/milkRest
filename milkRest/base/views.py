from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


def getAllHeaders():
    _headers = Header.objects.all()
    headerList = []
    for _ in _headers:
        _data = HeaderSerializer(_).data
        headerList.append(_data)
    return headerList



# RETURNS TO USER

@api_view()
def index(request):
    # get headers
    headers = getAllHeaders()
    return Response({"headers":headers}, status = 200)