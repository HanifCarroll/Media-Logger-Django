from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import MediaObject
from .utils import get_thumbnail


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
        url = request.POST['url']
        if MediaObject.objects.filter(url=url):
            print("Object already exists.")
            return HttpResponse("Media object already exists.")

        # This info will be there
        media_object = MediaObject()
        media_object.url = url
        media_object.user = request.POST['username']
        media_object.service = request.POST['service_name']
        media_object.time_posted = request.POST['timestamp']

        # This info might not be there, so we use .get
        media_object.artist = request.POST.get('artist', '')
        media_object.title = request.POST.get('title', '')

        if media_object.service != 'Soundcloud':
            thumbnail_url = request.POST.get('thumbnail_url', '')
            if thumbnail_url is not '':
                media_object.thumbnail_url = get_thumbnail(thumbnail_url)

        media_object.save()
        print('Media object created')
        return HttpResponse('Media object successfully created.')
    except Exception as e:
        print(type(e), ': ', e)
        return HttpResponse("error: ", type(e), ' - ', str(e))
