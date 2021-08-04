from core.validators import validate_file_size, validate_file_format
from django.test import TestCase
from django.core.exceptions import ValidationError

class File:
    """
        class for image (file) simulation
        for tests purposes
    """
    def __init__(self, name, size):
        self.name = name
        self.size = size

class ValidatorsTestCase(TestCase):

    def setUp(self):
        self.allowed_images = [File('test.png', 11), File('test.jpg', 20), File('test.jpeg', 10), File('test.gif', 15)]
        self.not_allowed_images = [File('test.zip', 20), File('test.raw', 10), File('test.bmp', 12)]
        self.big_image = File('test.png', 100000000000000)

