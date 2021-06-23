# Create your views here.
from ipware import get_client_ip
from requests import Session
from rest_framework import viewsets
from rest_framework.response import Response


class ReceiverViewSet(viewsets.ViewSet):
    def create(self, request):
        client_ip, is_routable = get_client_ip(request)
        session = Session()
        response = session.post(f'http://ip-api.com/json/{client_ip}')
        json = response.json()
        if json['status'] == 'success':
            return Response(json['country'])
        else:
            return Response('500')
