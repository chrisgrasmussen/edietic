from django.http import HttpResponse
from django.http import JsonResponse
from .models import Start
from.serializers import StartSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def start_list(request, format=None):
    
    #get all the starts
    #serialize them
    #return json
    
    if request.method == 'GET':
        starts = Start.objects.all()
        serializer = StartSerializer(starts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def start_detail(request, pk, format=None):
    
    start = Start.objects.get(id=pk)
    
    if request.method == 'GET':
        serializer = StartSerializer(start)
        return Response(serializer.data)
            
    elif request.method == 'PUT':
        serializer = StartSerializer(start, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        start.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

