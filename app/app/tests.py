from django.test import TestCase
from app.calc import add, subtract

class CaluTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)
    
    def test_add_numbers(self):
        self.assertEqual(subtract(5, 2),3)