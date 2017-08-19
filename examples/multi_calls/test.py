from unittest import TestCase
import mock
from examples.multi_calls.example import foo


class TestFoo(TestCase):
    @mock.patch('examples.multi_calls.example.bar')
    def test_foo(self, dummy_bar):
        foo(10)
        expected_calls = [mock.call(i) for i in range(0, 10, 2)]
        self.assertEqual(expected_calls, dummy_bar.call_args_list)
        dummy_bar.assert_has_calls(expected_calls)