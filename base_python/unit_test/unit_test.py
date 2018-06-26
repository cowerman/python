import unittest

def get_format_name(first, last):
    full_name = first +' '+ last
    return full_name.title()


def get_mid_name(first, mid, last):
    full_name = first +' '+ mid+' '+ last
    return full_name.title()


class TestNameFormat(unittest.TestCase):

    def test_first_last_name(self):
        format_name = get_format_name('mei', 'tong')
        self.assertEqual(format_name, 'Mei Tong')

    def test_mid_name(self):
        mid_name = get_mid_name('lu', 'hai', 'peng')
        self.assertEqual(mid_name, 'lu hai peng')

unittest.main()

