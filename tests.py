from django.contrib.auth.models import User
from django.test import TestCase
from mysite.models import Trigger
USERNAME = 'Anton'
PASSWORD = 'Dialog2011'


class TestShop(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username=USERNAME,
            is_superuser=True,
            password=PASSWORD
        )

    def Test_Create_Trigger(self):
        self.client.post(
            '/user/login/',
            {'username': USERNAME, 'password': PASSWORD}
        )
        response = self.client.post('/trigger/', {
            'trigger_price': 7000,
            'telegram_id': 12345678
        }, follow=True)

        new_trigger = Trigger.objects.get(trigger_price=7000, telegram_id=12345678)
        self.assertEqual(new_trigger.trigger_price, 7000)
        self.assertEqual(new_trigger.telegram_id, 12345678)


