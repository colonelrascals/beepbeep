from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

# Create your tests here.


from .models import Beep


User = get_user_model()

class BeepModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username='patrickkkkkk')

    def test_beep_item(self):
        obj = Beep.objects.create(
                user= User.objects.first(),
                content='Some random content'
            )
        self.assertTrue(obj.content == "Some random content")
        self.assertTrue(obj.id == 1)
        #self.assertEqual(obj.id, 1)
        absolute_url = reverse("beep:detail", kwargs={"pk": 1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_beep_url(self):
        obj = Beep.objects.create(
                user= User.objects.first(),
                content='Some random content'
            )
        absolute_url = reverse("beep:detail", kwargs={"pk": obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)