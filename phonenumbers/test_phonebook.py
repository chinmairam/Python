import unittest

from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        pass
    
    def test_lookup_by_name(self):
        #phonebook = PhoneBook()
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        #phonebook = PhoneBook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # Skipping a testcase
    @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        #phonebook = PhoneBook()
        self.assertTrue(self.phonebook.is_consistent())

# In phonenumbers directory, run python -m unittest
