import boto3
import urllib
import time

from PIL import Image
from io import BytesIO


def get_thumbnail(thumbnail_url):
    image = Image.open(urllib.request.urlopen(thumbnail_url))
    image.thumbnail((200, 200))

    img_io = BytesIO()
    image.save(img_io, format='JPEG')
    img_bytes = img_io.getvalue()

    file_name = "{:1f}".format(time.time()).replace('.', '') + ".jpeg"
    boto3.resource('s3').Bucket(
        'discord-media-log-thumbnails').put_object(
            Key=file_name,
            Body=img_bytes,
            ContentType='image/jpeg'
    )

    url = f'https://s3.us-east-2.amazonaws.com/discord-media-log-thumbnails/{file_name}'
    return url
