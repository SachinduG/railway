from rest_framework.decorators import api_view
from rest_framework.response import Response

from chat import get_response, get_sa


@api_view(['GET'])
def getChat():
    return Response("Welcome to Canis care Vet bot!")


@api_view(['POST'])
def getPredict(request):
    data = request.data
    print(data.list())
    if 'message' in request.data:
        message = request.data['message']
    else:
        message = "Hi1"
    #message = request.data.get('message', data)
    output = get_response(message)
    sa = get_sa(message)
    result = output+", "+str(sa)
    return Response(result)



