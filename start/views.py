from django.http import HttpResponse
from django.http import JsonResponse
from .models import Start
from.serializers import StartSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

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
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

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

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def index(request):
    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )