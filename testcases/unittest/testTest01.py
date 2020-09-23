import unittest


class FirstTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("setup...........")

    def test01(self):
        self.assertEqual(1 + 2, 3)

    def test02(self):
        self.assertGreaterEqual(5, 4)

    def test03(self):
        self.assertGreaterEqual(1, 4)

    def aaa(self):
        print("aaaaaa")

    def tearDown(self) -> None:
        print("teardown..........")


if __name__ == '__main__':
    unittest.main()
