from datetime import datetime
from django.shortcuts import render
from django.conf import settings
import json
import logging as log

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CompilerAPIModel
from .serializers import CompilerAPIModelSerializer


def setup_custom_logger(name):
    formatter = log.Formatter(fmt='%(asctime)s - %(process)d - %(levelname)s - %(message)s')
    handler = log.StreamHandler()
    handler.setFormatter(formatter)
    logger = log.getLogger(name)
    logger.setLevel(log.INFO)
    logger.addHandler(handler)
    return logger


logger = setup_custom_logger("api_face_recog")

def home(request):
    template = "app_home/html/homepage.html"
    context = {
        "lang_config":json.dumps(settings.LANG_CONFIG_FILE)
    }
    return render(request,template,context)

"""
####################################################
                    API
####################################################
"""

# GET COMPILER RESPONSE AFTER SUCCESSFUL CODE COMPILATION
class CompilerResponseApi(APIView):
    queryset = CompilerAPIModel
    serializer_class = CompilerAPIModelSerializer

    def get(self, request,*args, **kwargs):
        response = {
            "ERROR":"Invalid Request(Method : GET)"
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # start = datetime.now()
        API_URL = request.api_url
        print("API_URL: ", API_URL)
        # print(request.data)

        data = []
        status = "failure"
        message = "Invalid Data!!!"

        json_response = {
            "status":status,
            "message":message,
            "response":data,
        }
        return Response(json_response,status=status.HTTP_200_OK)