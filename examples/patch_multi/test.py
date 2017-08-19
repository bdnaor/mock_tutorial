from unittest import TestCase

import mock

from examples.patch_multi.example import my_method


class TestMultiple(TestCase):
    @mock.patch.multiple('examples.patch_multi.example',
                         foo=mock.DEFAULT,
                         bar=mock.DEFAULT)
    def test_my_method(self, foo, bar):
        foo.return_value = 'dummy_foo'
        bar.return_value = 'dummy_bar'

        self.assertEqual(my_method(), ('dummy_foo', 'dummy_bar'))
