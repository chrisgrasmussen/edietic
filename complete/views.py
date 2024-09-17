from django.http import HttpResponse
from django.http import JsonResponse
from .models import Complete
from.serializers import CompleteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def complete_list(request, format=None):
    if request.method == 'GET':
        completes = Complete.objects.all()
        serializer = CompleteSerializer(completes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CompleteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def complete_detail(request, pk, format=None):
    complete = Complete.objects.get(id=pk)
    
    if request.method == 'GET':
        serializer = CompleteSerializer(complete)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        serializer = CompleteSerializer(complete, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        complete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
