from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):  
    def setUp(self):  
        self.browser = webdriver.Firefox()  

    def tearDown(self):  
        self.browser.quit(
        )

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])


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
        self.check_for_row_in_list_table("1: OS Project 2")


        # There is still a text box inviting her to add another item.
        # She enters "Internetworking Lab 6"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Internetworking Lab 6")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.check_for_row_in_list_table("1: OS Project 2")
        self.check_for_row_in_list_table("2: Internetworking Lab 6")

        # Satisfied, she closes the browser.


if __name__ == "__main__":  
    unittest.main()  


