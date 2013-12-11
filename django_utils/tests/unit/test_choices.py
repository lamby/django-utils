from django.conf import settings

settings.configure(
    CACHES={},
    DATABASES={}
)

from django_utils.choices import get_choice_by_id, get_id_by_nice_name, \
        get_short_name_by_id, get_short_name_by_nice_name
from model_utils import Choices
from unittest import TestCase


TEST_CHOICES = Choices(
    (1, 'choice1', ('Choice 1')),
    (2, 'choice2', ('Choice 2')),
)


class Choices(TestCase):
    def test_get_choice_by_nice_name(self):
        id = get_id_by_nice_name(TEST_CHOICES, 'Choice 1')
        self.assertTrue(id == 1)

    def test_get_choice_by_id_not_in_index(self):
        c = get_choice_by_id(TEST_CHOICES, 2)
        self.assertTrue(c[0] == 2)
        self.assertTrue(c[1] == 'Choice 2')
        
    def test_get_short_name_by_id(self):
        name = get_short_name_by_id(TEST_CHOICES, 1)
        self.assertEqual(name, 'choice1')
        
    def test_get_short_name_by_nice_name(self):
        name = get_short_name_by_nice_name(TEST_CHOICES, 'Choice 1')
        self.assertEqual(name, 'choice1')
