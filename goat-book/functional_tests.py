from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


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
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text  
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")  
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She types "OS Project 2" into a text box
        inputbox.send_keys("OS Project 2") 

        # When she hits enter, the page updates, and now the page lists
        # "1: OS Project 2" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)  
    
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")  
        self.assertTrue(any(row.text == "1: OS Project 2" for row in rows))

        # There is still a text box inviting her to add another item.
        # She enters "Internetworking Lab 6"
        self.fail("Finish the test!")

        # The page updates again, and now shows both items on her list

        # Satisfied, she closes the browser.


if __name__ == "__main__":  
    unittest.main()  


