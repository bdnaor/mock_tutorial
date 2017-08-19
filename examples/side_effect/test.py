from mock import patch
from examples.patch_object.example import Application
from unittest import TestCase


class TestGetNextPerson(TestCase):
    @patch.object(Application, 'get_random_user')
    def test_get_next_person(self, mock_get_random_person):
        # arrange
        app = Application()
        user = {'people_seen': ['Sarah', 'Mary']}
        expected_person = 'Katie'
        mock_get_random_person.side_effect = ['Mary', 'Sarah', expected_person]

        # action
        actual_person = app.get_next_person(user)

        # assert
        self.assertEquals(expected_person, actual_person)
