from django.core.serializers import json as jsons
from django.http import HttpResponse, JsonResponse
from .models import Homework
import json
from .boilerplate import Boilerplate
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    all_homework = Homework.objects.all()
    jsonBody = Boilerplate.querytojson(all_homework)
    return HttpResponse(jsonBody)


def detail(request, homework_id):
    return HttpResponse("You're looking at homework %s" % homework_id)

@csrf_exempt
def homeworkRequest(request):
    if request.method == "POST":
        jsonBody = Boilerplate.decode_request_body(request.body)
        print(jsonBody["title"])

    # return HttpResponse(jsonBody)
    return JsonResponse(jsonBody)
