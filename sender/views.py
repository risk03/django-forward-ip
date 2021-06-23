from requests import Session
from rest_framework import viewsets
# Create your views here.
from rest_framework.response import Response


class SenderViewSet(viewsets.ViewSet):
    def create(self, request):
        session = Session()
        res1 = session.post(
            'http://127.0.0.1:8000/receiver/',
            headers={'X-Forwarded-For': '2.12.12.12'}
        )
        res2 = session.post(
            'http://127.0.0.1:8000/receiver/',
            headers={'HTTP-X-Forwarded-For': '2.12.12.12'}
        )
        return Response([res1.json(), res2.json()])
