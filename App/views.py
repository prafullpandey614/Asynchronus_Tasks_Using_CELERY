from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
# Create your views here.

class OverviewCreateAPIView(APIView):
    
    def get(self,request):
        response = {
            "/upload" : "Uplaod A Video",
            "/convert/id" : "Covert the video",
            "download" : "Download the video",
        }
        return Response(response)