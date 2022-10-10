from rest_framework.decorators import api_view
from rest_framework.response import Response

from chat import get_response, get_sa


@api_view(['GET'])
def getChat():
    return Response("Welcome to Canis care Vet bot!")


@api_view(['POST'])
def getPredict(request):
    data = request.body
    print(data)
    print(request.body['message'])
    if 'message' in request.data:
        message = request.body['message']
    else:
        message = "Hi"
    #message = request.data.get('message', data)
    print(message)
    output = get_response(message)
    sa = get_sa(message)
    result = output+", "+str(sa)
    return Response(result)



