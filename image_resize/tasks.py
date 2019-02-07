from __future__ import absolute_import, unicode_literals

from .models import NewImage
from celery import shared_task, task
from PIL import Image
from io import BytesIO, StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from main.celery import app
import base64

import logging

logger = logging.getLogger(__name__)


@app.task
def resize(data):
    filename, w, h = data
    image = Image.open(filename)
    old_size = image.size
    image = image.resize((int(w), int(h)), Image.ANTIALIAS)
    output = BytesIO()
    image.save(output, format='JPEG')
    file = InMemoryUploadedFile(ContentFile(output.getvalue()), None, 'image.jpg', 'image/jpeg', image.size, None)
    o_h, o_w = old_size
    NewImage(image=file, old_width=o_w, old_height=o_h,).save()
    new_size = image.size
    logger.info('old_size: {} {} new_size: {} {}'.format(*old_size, *new_size))
    return old_size, new_size


@app.task
def alt(image):
    i = Image.open(base64.b64encode(image))
    return i.size
