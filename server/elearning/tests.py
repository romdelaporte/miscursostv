from django.test import LiveServerTestCase
from selenium import webdriver

from django.contrib.auth.models import User

import time


class MySeleniumTests(LiveServerTestCase):
    # fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome(executable_path='./chromedriver')
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        username = 'mysuperuser'
        email = 'testing@testing.com'
        password = 'mysecretpassword7'

        my_admin = User.objects.create_superuser(username=username, email=email, password=password)
        my_admin.save()
        
        self.selenium.get('http://localhost:8000/accounts/login')
        username_input = self.selenium.find_element_by_id("id_username")
        password_input = self.selenium.find_element_by_id("id_password")

        username_input.send_keys(username)
        password_input.send_keys(password)
        self.selenium.find_element_by_xpath("//input[@type='submit']").click()

        time.sleep(6)