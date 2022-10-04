from django.shortcuts import render
from django.conf import settings
import json

def home(request):
    template = "app_home/html/homepage.html"
    context = {
        "lang_config":json.dumps(settings.LANG_CONFIG_FILE)
    }
    return render(request,template,context)
