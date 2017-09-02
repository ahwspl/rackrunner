# Django imports
from rest_framework import viewsets
from rest_framework.response import Response
# Application imports


class RackerView(viewsets.ViewSet):

    authentication_classes = ()

    def getWarehousePath(self, request):
        rack_ids = request.GET['racks']
        print(rack_ids)
        return Response({'msg':'Request successfully queued'})