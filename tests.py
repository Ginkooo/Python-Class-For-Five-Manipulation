from five import Five
import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.five = Five()

    def test_operations_on_five(self):
        self.assertEqual(5 * 3, self.five * 3)
        self.assertEqual(3 * 5, 3 * self.five)
        self.assertEqual(5 + 3, self.five + 3)
        self.assertEqual(3 + 5, 3 + self.five)
        self.assertEqual(5 - 3, self.five - 3)
        self.assertEqual(3 - 5, 3 - self.five)
        self.assertEqual(5 / 3, self.five / 3)
        self.assertEqual(3 / 5, 3 / self.five)
        self.assertEqual(5 // 3, self.five // 3)
        self.assertEqual(3 // 5, 3 // self.five)
        self.assertEqual(5 ** 3, self.five ** 3)
        self.assertEqual(3 ** 5, 3 ** self.five)
        self.assertEqual(5 << 3, self.five << 3)
        self.assertEqual(5 >> 3, self.five >> 3)
        self.assertEqual(-5, -self.five)
        self.assertEqual(+5, +self.five)
        self.assertEqual(abs(5), abs(self.five))
        self.assertEqual(~5, ~self.five)
        self.assertEqual(complex(5), complex(self.five))
        self.assertEqual(5 < 3, self.five < 3)
        self.assertEqual(5 <= 3, self.five <= 3)
        self.assertEqual(5 == 3, self.five == 3)
        self.assertEqual(5 != 3, self.five != 3)
        self.assertEqual(5 >= 3, self.five >= 3)
        self.assertEqual(5 > 3, self.five > 3)
        self.assertEqual(self.five.say_five_in_language('Polish'), 'pięć')
        self.assertEqual(self.five.say_five_times('😊'), '😊😊😊😊😊')
        self.assertEqual(self.five.say_five_times('😹'), '😹😹😹😹😹')
        self.assertEqual(self.five.say_five_times('vodka'), 'vodkavodkavodkavodkavodka')
        self.assertEqual(self.five.get_five_in_digit_type('vodka'), '5')
        self.assertEqual(self.five.get_five_in_digit_type('European'), '5')
        self.assertEqual(self.five.get_five_in_digit_type('Arabic'), '٥')
        self.assertEqual(self.five.get_five_in_digit_type('Arabic-west'), '۵')
