from mock import patch
from examples.patch.example import get_next_person
from unittest import TestCase


class TestGetNextPerson(TestCase):
    @patch('examples.patch.example.get_random_user')
    def test_get_next_person(self, mock_get_random_person):
        # arrange
        user = {'people_seen': []}
        expected_person = 'Katie'
        mock_get_random_person.return_value = expected_person

        # action
        actual_person = get_next_person(user)

        # assert
        self.assertEquals(expected_person, actual_person)


