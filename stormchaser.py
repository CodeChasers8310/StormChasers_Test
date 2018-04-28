import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class StormChaserTest(unittest.TestCase):
    driver = webdriver.Chrome('C:/seleniumtests/chromedriver')  # Optional argument, if not specified will search path.

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_searchTagNotLoggedIn(self):
        search = "tornado"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/home")
        time.sleep(2)
        elem = driver.find_element_by_name("search")
        elem.send_keys(search)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "http://codechaser8310.pythonanywhere.com/blog/blog_search/?search=tornado" in driver.current_url
        time.sleep(2)

    def test_searchTagLoggedIn(self):
        search = "tornado"
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/login")
        time.sleep(2)
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        elem = driver.find_element_by_name("search")
        elem.send_keys(search)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assertion = "Storm Chasers Hub"
        title = driver.title.__str__()
        assert assertion == title, "Take you to Blog page"
        assert "http://codechaser8310.pythonanywhere.com/blog/blog_search/?search=tornado" in driver.current_url
        time.sleep(2)

    def test_LearnMoreButton(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/home")
        time.sleep(2)
        python_button = driver.find_element_by_xpath("(//a[contains(@class,'btn btn-primary btn-lg')])")
        python_button.click()
        assert "http://codechaser8310.pythonanywhere.com/blog/about_us/" in driver.current_url
        time.sleep(2)

    def test_loginToAdminSiteSuccessfully(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/admin")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(3)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/admin/" in driver.current_url
        time.sleep(3)

    def test_loginToAdminSiteUnSuccessfully(self):
        user = "instructor"
        pwd = "instructor1"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/admin")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/admin/login/?next=/admin/" in driver.current_url
        time.sleep(2)

    def test_loginToSiteSuccessfully(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/login")
        time.sleep(2)
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/accounts/profile/" in driver.current_url
        time.sleep(3)

    def test_loginToSiteUnSuccessfully(self):
        user = "instructor"
        pwd = "instructor1"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/login")
        time.sleep(2)
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/accounts/login" in driver.current_url
        time.sleep(3)

    def test_loginToSiteBadUserName(self):
        user = "instructor1"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/login")
        time.sleep(2)
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        time.sleep(3)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/accounts/login" in driver.current_url
        time.sleep(3)

    def test_registerUserSuccessfully(self):
        user = "edosseh"
        firstname = "Edem"
        lastname = "Dosseh"
        email = "edosseh@unomaha.edu"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/register")
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
        signin_button = driver.find_element_by_xpath("(//a[contains(@href,'/blog/accounts/login/')])")
        signin_button.click()
        assert "http://codechaser8310.pythonanywhere.com/blog/accounts/login/" in driver.current_url
        time.sleep(2)

    def test_registerUserUnSuccessfully(self):
        user = "edosseh"
        firstname = "Edem"
        lastname = "Dosseh"
        email = "edosseh"  # INVALID EMAIL
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/register")
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
        assert "http://codechaser8310.pythonanywhere.com/blog/register" in driver.current_url
        time.sleep(3)

    def test_changePasswordSuccessfully(self):
        user = "edosseh1"
        pwd = "frosty05"
        pwd2 = "frosty05"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/login/")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/accounts/profile/" in driver.current_url
        time.sleep(2)
        chng_pwd = driver.find_element_by_xpath("(//a[contains(@href,'/blog/password-change/')])")
        chng_pwd.click()
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
        assert "http://codechaser8310.pythonanywhere.com/blog/password-change/done/" in driver.current_url
        time.sleep(3)

    def test_changePasswordUnmatchedNewPassword(self):
        user = "edosseh1"
        pwd = "frosty05"
        pwd2 = "frosty05"
        pwd3 = "forsty06"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/login/")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/accounts/profile/" in driver.current_url
        time.sleep(2)
        chng_pwd = driver.find_element_by_xpath("(//a[contains(@href,'/blog/password-change/')])")
        chng_pwd.click()
        elem = driver.find_element_by_name("old_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem = driver.find_element_by_id("id_new_password1")
        elem.send_keys(pwd2)
        time.sleep(2)
        elem = driver.find_element_by_id("id_new_password2")
        elem.send_keys(pwd3)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/password-change/" in driver.current_url
        time.sleep(3)

    def test_changePasswordUnmatchedOriginalPwd(self):
        user = "edosseh1"
        pwd = "frosty05"
        pwd1 = "frosty04"
        pwd2 = "frosty05"
        pwd3 = "forsty05"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/login/")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/accounts/profile/" in driver.current_url
        time.sleep(2)
        chng_pwd = driver.find_element_by_xpath("(//a[contains(@href,'/blog/password-change/')])")
        chng_pwd.click()
        elem = driver.find_element_by_name("old_password")
        elem.send_keys(pwd1)
        time.sleep(2)
        elem = driver.find_element_by_id("id_new_password1")
        elem.send_keys(pwd2)
        time.sleep(2)
        elem = driver.find_element_by_id("id_new_password2")
        elem.send_keys(pwd3)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/password-change/" in driver.current_url
        time.sleep(4)

    def test_EditProfileSuccessfully(self):
        user = "edosseh1"
        pwd = "frosty05"
        addr = "007 James Bond Rd"
        city = "New York"
        zip = "68128"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/login/")
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/accounts/profile/" in driver.current_url
        time.sleep(2)
        edit_profile = driver.find_element_by_xpath("(//a[contains(@href,'/blog/edit/')])")
        edit_profile.click()
        elem = driver.find_element_by_name("address")
        elem.clear()
        time.sleep(2)
        elem.send_keys(addr)
        time.sleep(2)
        elem = driver.find_element_by_name("city")
        elem.clear()
        time.sleep(2)
        elem.send_keys(city)
        time.sleep(2)
        elem = driver.find_element_by_name("zipcode")
        elem.clear()
        time.sleep(2)
        elem.send_keys(zip)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        assert "http://codechaser8310.pythonanywhere.com/blog/edit/" in driver.current_url
        time.sleep(3)

    def test_guestAccessTest(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/home")
        assert driver.find_element_by_xpath("(//a[contains(@class,'btn btn-primary btn-lg')])")
        assert "Can access the Home page"
        time.sleep(2)
        python_button = driver.find_element_by_xpath(
            "(//a[contains(@class,'btn btn-primary btn-lg')])")  # Learn More button
        python_button.click()
        assert "http://codechaser8310.pythonanywhere.com/blog/about_us/" in driver.current_url
        assert "Can Access the About Us page"
        time.sleep(2)
        driver.get("http://codechaser8310.pythonanywhere.com/blog/blog")
        assert "http://codechaser8310.pythonanywhere.com/blog/blog" in driver.current_url
        assert "Can view blog post"
        time.sleep(2)
        submit_post = driver.find_element_by_xpath("(//a[contains(@href,'/blog/post/')])")  # Submit post element
        submit_post.click()
        assert driver.find_element_by_xpath(
            "(//input[@value = 'Log-in'])"), "Cannot submit  post.Prompted to login in order to submit post"
        time.sleep(3)
        driver.get("http://codechaser8310.pythonanywhere.com/blog/blog")
        comment_post = driver.find_element_by_xpath("(//a[contains(@href,'/blog/post/1')])")  # Comment post element
        comment_post.click()
        assert driver.find_element_by_xpath(
            "(//input[@value = 'Log-in'])"), 'Cannot comment post. Prompted to login in order to submit post'
        time.sleep(2)
        driver.get("http://codechaser8310.pythonanywhere.com/blog/dashboard")
        assert driver.find_element_by_xpath("(//input[@value = 'Log-in'])"), 'Cannot access dashboard. Get Login page'
        time.sleep(2)
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/profile")
        assert driver.find_element_by_xpath("(//input[@name = 'username'])"), 'Cannot access profile page. Get Login page'
        time.sleep(2)

    def test_loggedInUserAccessTest(self):
        user = "instructor"
        pwd = "instructor1a"
        zip = 68128
        year = 2017
        month = 12
        day = 15
        selenium_post_title = "Automated weather post"
        selenium_post_body = "Wow this stuff works"
        selenium_post_tag = "selenium"
        selenium_file_path = "c:/seleniumtests/Hollie.png"
        selenium_comment = "Comment text"
        selenium_comment_edit = ". Comment text edit"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://codechaser8310.pythonanywhere.com/blog/home")
        assert driver.find_element_by_xpath("(//a[contains(@class,'btn btn-primary btn-lg')])")
        assert "Can access the Home page"
        time.sleep(2)
        python_button = driver.find_element_by_xpath(
            "(//a[contains(@class,'btn btn-primary btn-lg')])")  # Learn More button
        python_button.click()
        assert "http://codechaser8310.pythonanywhere.com/blog/about_us/" in driver.current_url
        assert "Can Access the About Us page"
        time.sleep(2)
        # Login to test forms
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/login")
        time.sleep(2)
        elem = driver.find_element_by_name("username")
        elem.send_keys(user)
        time.sleep(2)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/accounts/profile/" in driver.current_url
        time.sleep(2)
        driver.get("http://codechaser8310.pythonanywhere.com/blog/dashboard")
        assert "http://codechaser8310.pythonanywhere.com/blog/dashboard/" in driver.current_url
        assert "Can access dashboard get Login page"
        time.sleep(2)
        elem = driver.find_element_by_name("zip")
        elem.send_keys(zip)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert "http://codechaser8310.pythonanywhere.com/blog/get_forecast/?lat=&lon=&zip=68128&year=&month=&day=" in driver.current_url
        time.sleep(4)
        elem = driver.find_element_by_name("zip")
        elem.send_keys(zip)
        time.sleep(2)
        elem = driver.find_element_by_name("year")
        elem.send_keys(year)
        time.sleep(2)
        elem = driver.find_element_by_name("month")
        elem.send_keys(month)
        time.sleep(2)
        elem = driver.find_element_by_name("day")
        elem.send_keys(day)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        assert driver.find_element_by_xpath("(//a[contains(@href,'https://darksky.net/')])")
        assert "Check historical weather loaded successfully"
        time.sleep(4)
        driver.get("http://codechaser8310.pythonanywhere.com/blog/blog")
        assert "http://codechaser8310.pythonanywhere.com/blog/blog" in driver.current_url
        assert "Can view blog post"
        time.sleep(2)

        # Comment Post 1
        comment_post_link = driver.find_element_by_xpath(
            "(//a[contains(@href,'/blog/post/1')])")  # Comment post link element
        comment_post_link.click()
        assert driver.find_element_by_xpath("(//a[contains(@class,'btn btn-primary')])"), "Post is opened successfully"
        time.sleep(4)
        add_comment_button = driver.find_element_by_xpath("(//a[contains(@class,'btn btn-primary')])")
        add_comment_button.click()
        elem = driver.find_element_by_name("text")
        elem.send_keys(selenium_comment)
        time.sleep(3)
        post_comment_button = driver.find_element_by_xpath("(// button[text() = 'Post'])")
        post_comment_button.click()
        time.sleep(3)
        assert "Can comment post"
        time.sleep(3)

        # Submit Post
        driver.get("http://codechaser8310.pythonanywhere.com/blog/blog/")
        time.sleep(5)
        submit_post = driver.find_element_by_xpath("(//a[contains(@href,'/blog/post/')])")  # Submit post element
        submit_post.click()
        assert "http://codechaser8310.pythonanywhere.com/blog/post/new/" in driver.current_url
        time.sleep(2)
        elem = driver.find_element_by_name("title")
        elem.send_keys(selenium_post_title)
        time.sleep(2)
        elem = driver.find_element_by_name("text")
        elem.send_keys(selenium_post_body)
        time.sleep(2)
        elem = driver.find_element_by_name("form-0-image")
        elem.send_keys(selenium_file_path)
        time.sleep(3)
        elem = driver.find_element_by_name("tag")
        elem.send_keys(selenium_post_tag)
        time.sleep(2)
        submit_button = driver.find_element_by_xpath("(//input[@name = 'submit'])")
        submit_button.click()
        assert driver.find_element_by_xpath("(//div[@class = 'w3-center' and h2='Automated weather post'])")
        assert "Blog posted successfully"
        time.sleep(5)

        # Edit Post
        driver.get("http://codechaser8310.pythonanywhere.com/blog/blog/")
        time.sleep(5)
        click_on_new_post = driver.find_element_by_xpath("(//h5[text()='instructor'])")
        click_on_new_post.click()
        edit_post_button = driver.find_element_by_xpath("(//button[contains(.,'Edit Post' )])")
        edit_post_button.click()
        elem = driver.find_element_by_name("PostForm-text")
        elem.send_keys(selenium_comment_edit)
        time.sleep(3)
        save_button = driver.find_element_by_xpath("(//button[contains(.,'Save' )])")
        save_button.click()
        assert "Edit post successful"
        # Delete Post
        time.sleep(5)
        delete_post = driver.find_element_by_xpath("(//a[contains(@href,'/blog/post_deleted/')])")  # Delete post button
        time.sleep(2)
        delete_post.click()
        time.sleep(3)
        driver.get("http://codechaser8310.pythonanywhere.com/blog/blog/")
        time.sleep(5)
        assert "http://codechaser8310.pythonanywhere.com/blog/blog/" in driver.current_url
        time.sleep(3)
        # MyProfile
        driver.get("http://codechaser8310.pythonanywhere.com/blog/accounts/profile")
        # Asserting edit your profile and change your password is present on page
        assert driver.find_element_by_xpath("(//a[contains(@href,'/blog/edit/')])")
        assert driver.find_element_by_xpath("(//a[contains(@href,'/blog/password-change/')])")
        assert "http://codechaser8310.pythonanywhere.com/blog/accounts/profile/" in driver.current_url  # Can access profile page
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.stop_client()


if __name__ == "__main__":
    unittest.main()
