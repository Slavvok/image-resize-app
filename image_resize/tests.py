from django.test import TestCase
from image_resize.tasks import resize
from main.celery import app
# Create your tests here.


class TestResizeTask(TestCase):
    def setUp(self):
        app.conf.update(CELERY_ALWAYS_EAGER=True)

    def test(self):
        resize(('tests/image.jpg', 100, 30))
