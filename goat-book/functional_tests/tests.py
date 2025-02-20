
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.common.exceptions import WebDriverException



MAX_WAIT = 5


class NewVisitorTest(LiveServerTestCase):  
    def setUp(self):  
        self.browser = webdriver.Firefox()  

    def tearDown(self):  
        self.browser.quit(
        )

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:  
            try:
                table = self.browser.find_element(By.ID, "id_list_table")  
                rows = table.find_elements(By.TAG_NAME, "tr")
                self.assertIn(row_text, [row.text for row in rows])
                return  
            except (AssertionError, WebDriverException):  
                if time.time() - start_time > MAX_WAIT:  
                    raise  
                time.sleep(0.5)


    def test_can_start_a_todo_list(self):  
        # Risha wants to use a to-do app to track her school assignments on her browser.

        # She goes to it's homepage as it is a web-app.
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table("1: OS Project 2")


        # There is still a text box inviting her to add another item.
        # She enters "Internetworking Lab 6"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Internetworking Lab 6")
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table("1: OS Project 2")
        self.wait_for_row_in_list_table("2: Internetworking Lab 6")

        # Satisfied, she closes the browser.
