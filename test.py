import unittest
from hello import send_email


class TestMultipleMailSend(unittest.TestCase):
    def test_mail(self):
        i = 0
        while i != 100:
            print(i)
            send_email.delay()
            i = i + 1


if __name__ == '__main__':
    unittest.main()