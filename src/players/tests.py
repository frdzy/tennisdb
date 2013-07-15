from django.test import TestCase
from models import Player, Gender

import datetime


class PlayerTestCase(TestCase):
    def setUp(self):
        self.test_user_no_gender = Player(
            first_name='Player',
            last_name='One',
            birthday=datetime.date(1900, 1, 1)
        )

    def test_age_calculation(self):
        player = self.test_user_no_gender

        today = datetime.date.today()
        self.assertEqual(today - player.birthday, player.age())

    def test_default_gender(self):
        player = self.test_user_no_gender

        self.assertEqual(Gender.UNKNOWN, player.gender)
