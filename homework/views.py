from django.core.serializers import json
from django.http import HttpResponse, JsonResponse
from .models import Homework

# Create your views here.
def index(request):
    all_homework = []
    all_homework = Homework.objects.all()
    json_serializer = json.Serializer()
    json_serialized = json_serializer.serialize(all_homework)
    return HttpResponse(json_serialized)

def detail(request, homework_id):
    return HttpResponse("You're looking at homework %s" % homework_id)
