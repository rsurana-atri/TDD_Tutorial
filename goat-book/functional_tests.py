import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):  
    def setUp(self):  
        self.browser = webdriver.Firefox()  

    def tearDown(self):  
        self.browser.quit()


    def test_can_start_a_todo_list(self):  
        # Risha wants to use a to-do app to track her school assignments on her browser.

        # She goes to it's homepage as it is a web-app.
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)  

        # She is invited to enter a to-do item straight away
        self.fail("Finish the test!")  

        # She types "OS Project 2" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1: OS Project 2" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Internetworking Lab 6"

        # The page updates again, and now shows both items on her list

        # Satisfied, she closes the browser.


if __name__ == "__main__":  
    unittest.main()  


