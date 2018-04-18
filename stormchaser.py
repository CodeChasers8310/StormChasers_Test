import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginToAdmin(unittest.TestCase):
    driver = webdriver.Chrome('C:/seleniumtests/chromedriver')  # Optional argument, if not specified will search path.

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_loginToAdmin(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In To Admin Page"
        time.sleep(2)

    def test_loginToSite(self):
        user = "edosseh"
        pwd = "frosty04"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login")
        time.sleep(2)
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In To Blog"
        time.sleep(2)

    def test_registerUser(self):
        user = "edosseh"
        firstname = "Edem"
        lastname = "Dosseh"
        email = "edosseh@unomaha.edu"
        pwd = "frosty04"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/register")
        time.sleep(2)
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_name("first_name")
        elem.send_keys(firstname)
        time.sleep(2)
        elem = driver.find_element_by_name("last_name")
        elem.send_keys(lastname)
        time.sleep(2)
        elem = driver.find_element_by_name("email")
        elem.send_keys(email)
        time.sleep(2)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem = driver.find_element_by_name("password2")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Registered"
        time.sleep(2)

    def test_passwordReset(self):
        email = "edosseh@unomaha.edu"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/password-reset/")
        time.sleep(2)
        elem = driver.find_element_by_name("email")
        elem.send_keys(email)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Password changed"
        time.sleep(2)

    def test_changePassword(self):
        user = "edosseh"
        pwd = "frosty04"
        pwd2 = "frosty05"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin/password_change/")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_name("old_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem = driver.find_element_by_id("id_new_password1")
        elem.send_keys(pwd2)
        time.sleep(2)
        elem = driver.find_element_by_id("id_new_password2")
        elem.send_keys(pwd2)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Password changed"
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.stop_client()


if __name__ == "__main__":
    unittest.main()
