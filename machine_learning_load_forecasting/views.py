from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


@api_view(["GET"])
def ideal_weight(request):
    try:
        return JsonResponse("I am very glad that this is working.", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

