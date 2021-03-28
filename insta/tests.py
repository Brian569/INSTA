from django.test import TestCase
from .models import Profile, Image

class ProfileTest(TestCase):

    def setUp(self):

        self.bmn = Profile(bio='Testing is awesome!')

    def test_instance(self):
        self.assertTrue(isinstance(self.bmn, Profile))

    def test_save(self):
        self.bmn.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    
class ImageTest(TestCase):

    def setUp(self):
        self.bmn = Profile(bio='Testing is awesome!')
        self.bmn.save_profile()

        self.new_image = Image(image_name='boom', image_caption='very important', profile=self.bmn, likes=12, comments='new comment')

        def tearDown(self):
            Image.objects.all().delete()
            Profile.objects.all().delete()

     