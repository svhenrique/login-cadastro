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


