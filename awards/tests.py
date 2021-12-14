from django.test import TestCase
from .models import   Project,Profile,Rating
from django.contrib.auth.models import User
import datetime as dt
# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):
        self.Art = Project(Project='Art')

    def test_instance(self):
        self.assertTrue(isinstance(self.Art,Project))

    def tearDown(self):
        Project.objects.all().delete()

    def test_save_method(self):
        self.Art.save_category()
        category = Project.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.Art.delete_category('Art')
        category = Project.objects.all()
        self.assertTrue(len(category)==0)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.Python = Profile(Profile='Python')

    def test_instance(self):
        self.assertTrue(isinstance(self.Python,Profile))

    def tearDown(self):
        Profile.objects.all().delete()

    def test_save_method(self):
        self.Python.save_Profile()
        technology = Profile.objects.all()
        self.assertTrue(len(technology)>0)

    def test_delete_method(self):
        self.Python.delete_Profile('Python')
        technology = Profile.objects.all()
        self.assertTrue(len(technology)==0)


class countriesTestClass(TestCase):
    def setUp(self):
        self.Kenya = countries(countries='Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya,countries))

    def tearDown(self):
        countries.objects.all().delete()

    def test_save_method(self):
        self.Kenya.save_country()
        country = countries.objects.all()
        self.assertTrue(len(country)>0)

    def test_delete_method(self):
        self.Kenya.delete_country('Kenya')
        country = countries.objects.all()
        self.assertTrue(len(country)==0)




class colorsTestClass(TestCase):
    def setUp(self):
        self.Black = colors(colors='Black')

    def test_instance(self):
        self.assertTrue(isinstance(self.Black,colors))

    def tearDown(self):
        colors.objects.all().delete()

    def test_save_method(self):
        self.Black.save_color()
        color = colors.objects.all()
        self.assertTrue(len(color)>0)

    def test_delete_method(self):
        self.Black.delete_color('Black')
        color = colors.objects.all()
        self.assertTrue(len(color)==0)
