from unittest import TestCase
from main_menu import Menu

__author__ = 'crswin5726'


class TestCatalog(TestCase):
    def setUp(self):
        self.choice = 1

    def test_init(self):
        self.assertEquals(self.image.columns, 2)
        self.assertEquals(self.image.rows, 2)

    def test_compute_histogram(self):
        self.image.compute_histogram()
        self.assertNotEquals(self.image.compute_histogram, {})

    def tearDown(self):
        del self.image