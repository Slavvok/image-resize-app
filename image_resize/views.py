from django.http import JsonResponse, FileResponse, HttpResponse
from image_resize.tasks import resize
from django.views.decorators.csrf import csrf_exempt
from django.core.files.uploadhandler import TemporaryUploadedFile

from celery.result import AsyncResult

import logging
logger = logging.getLogger(__name__)


@csrf_exempt
def index(request):
    if request.method == 'POST' and request.FILES['image']:
        h = request.POST['h']
        w = request.POST['w']
        file = request.FILES['image']
        try:
            with TemporaryUploadedFile(name=file.name, content_type='image/jpeg', size='image_size', charset='base64') as tf:
                tf.write(file.read())
                task = resize.delay((tf.name, w, h))
                logger.debug('Done')
                return JsonResponse(task.task_id, safe=False)
        except Exception as e:
            logger.error(e)
    else:
        return JsonResponse('None', safe=False)


@csrf_exempt
def status(request):
    if request.method == 'POST':
        task_id = request.POST['id']
        res = AsyncResult(task_id)
        task_status = res.status
        result = res.get(timeout=5, propagate=False)
        data = {'status': task_status,
                'result': result, }
        return JsonResponse(data, safe=False)
