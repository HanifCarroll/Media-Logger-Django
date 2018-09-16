from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import MediaObject


def index(request):
    query = MediaObject.objects.all().order_by('-time_posted')
    data = serializers.serialize("json", query)
    return HttpResponse(data, content_type="application/json")


def user(request, username):
    query = MediaObject.objects.filter(user=username).order_by('-time_posted')
    data = serializers.serialize("json", query)
    # return HttpResponse(response, content_type="application/json")
    return HttpResponse(data, content_type="application/json")


def service(request, service_name):
    query = MediaObject.objects.filter(
        service=service_name).order_by('-time_posted')
    data = serializers.serialize("json", query)
    return HttpResponse(data, content_type="application/json")


def user_service(request, username, service_name):
    query = MediaObject.objects.filter(
        user=username, service=service_name).order_by('-time_posted')
    data = serializers.serialize("json", query)
    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def create(request):
    try:
        if MediaObject.objects.filter(url=request.POST['url']):
            print("Object already exists.")
            return HttpResponse("Media object already exists.")

        media_object = MediaObject()
        media_object.url = request.POST['url']
        media_object.artist = request.POST['artist']
        media_object.title = request.POST['title']
        media_object.user = request.POST['username']
        media_object.service = request.POST['service_name']
        media_object.time_posted = request.POST['timestamp']

        if media_object.service != 'Soundcloud':
            media_object.thumbnail_url = request.POST['thumbnail_url']

        media_object.save()
        print('Media object created')
        return HttpResponse('Media object successfully created.')
    except Exception as e:
        print(e)
        return HttpResponse("error: " + str(e))
