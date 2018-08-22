from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json


@api_view(["POST"])
def ideal_weight(height):
    try:
        height = json.loads(height.body)
        weight = str(height * 10)
        return JsonResponse("Ideal weight should be:" + weight + " kg", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
