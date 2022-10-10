from rest_framework.decorators import api_view
from rest_framework.response import Response

from chat import get_response, get_sa


@api_view(['GET'])
def getChat():
    return Response("Welcome to Canis care Vet bot!")


@api_view(['POST'])
def getPredict(request):
    data = request.data
    dataList = list(data.values())
    print(dataList[1])
    msg = dataList[1]
    print(msg)
    message = msg['message']
    output = get_response(message)
    sa = get_sa(message)
    result = output+" | Sentiment Value is "+str(sa)
    return Response(result)



