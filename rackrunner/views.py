# Django imports
from rest_framework import viewsets
from django.http import JsonResponse
# Application imports
from rackrunner.co_ordinate import get_coordinate, get_boundary, get_path


class RackerView(viewsets.ViewSet):
    authentication_classes = ()

    def getWarehousePath(self, request):
        rack_ids = request.GET.getlist('racks')
        all_racks = get_coordinate()
        boundary = get_boundary()
        path = get_path(rack_ids)

        return JsonResponse({
            "path": path,
            "boundary" : boundary,
            "racks" : all_racks
        })
