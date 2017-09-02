import json

# Django imports
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
# Application imports
from rackrunner.co_ordinate import get_coordinate, get_boundary
class RackerView(viewsets.ViewSet):
    authentication_classes = ()

    def getWarehousePath(self, request):
        rack_ids = request.GET.get('racks',[])
        all_racks = get_coordinate()
        boundary = get_boundary()
        return JsonResponse({
            "boundary" : boundary,
            "racks" : all_racks
        })