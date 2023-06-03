from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Homework
import json

# Create your views here.
def index(request):
    all_homework = []
    all_homework = Homework.objects.all()
    json_data = json.dumps(all_homework, indent=4)
#    output = ", ".join([q.title for q in all_homework])
    return JsonResponse(json_data, content_type="application/json")

def detail(request, homework_id):
    return HttpResponse("You're looking at homework %s" % homework_id)
