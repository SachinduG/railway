from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from chat import get_response, get_sa


@api_view(['GET'])
def getChatBot(request):
    return Response("Welcome to Canis care Vet bot!")


@api_view(['POST'])
def getPrecdict(request):
    data = request.data
    print(data)
    message = data['message']
    output = get_response(message)
    sa = get_sa(message)
    result = output+","+str(sa)
    print(result)
    return Response(result)



