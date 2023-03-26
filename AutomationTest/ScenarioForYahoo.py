import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class YahooTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.yahoo.com/")
        self.assertIn("Yahoo", driver.title)
        elem = driver.find_element_by_id("uh-signin")
        elem.click()
        elem = driver.find_element_by_name("username")
        elem.send_keys("testuser@yahoo.com")
        elem = driver.find_element_by_name("password")
        elem.send_keys("testpass")
        elem.send_keys(Keys.RETURN)
        assert "Welcome" in driver.page_source

    def test_search(self):
        driver = self.driver
        driver.get("https://www.yahoo.com/")
        self.assertIn("Yahoo", driver.title)
        elem = driver.find_element_by_name("p")
        elem.send_keys("Python Programming Language")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_send_email(self):
        driver = self.driver
        driver.get("https://www.yahoo.com/")
        self.assertIn("Yahoo", driver.title)
        elem = driver.find_element_by_id("uh-mail-link")
        elem.click()
        elem = driver.find_element_by_id("login-username")
        elem.send_keys("testuser@yahoo.com")
        elem = driver.find_element_by_id("login-signin")
        elem.click()
        elem = driver.find_element_by_id("login-passwd")
        elem.send_keys("testpass")
        elem = driver.find_element_by_id("login-signin")
        elem.click()
        elem = driver.find_element_by_id("message-to-field")
        elem.send_keys("testrecipient@yahoo.com")
        elem = driver.find_element_by_id("message-subject")
        elem.send_keys("Test Email")
        elem = driver.find_element_by_id("rtetext")
        elem.send_keys("This is a test email.")
        elem = driver.find_element_by_id("send-button")
        elem.click()
        assert "Your message has been sent" in driver.page_source

    def test_change_password(self):
        driver = self.driver
        driver.get("https://www.yahoo.com/")
        self.assertIn("Yahoo", driver.title)
        elem = driver.find_element_by_id("uh-profile")
        elem.click()
        elem = driver.find_element_by_link_text("Account Info")
        elem.click()
        elem = driver.find_element_by_name("password")
        elem.send_keys("newpassword")
        elem = driver.find_element_by_name("save")
        elem.click()
        assert "Your changes have been saved" in driver.page_source

    def test_read_news(self):
        driver = self.driver
        driver.get("https://www.yahoo.com/")
        self.assertIn("Yahoo", driver.title)
        elem = driver.find_element_by_link_text("News")
        elem.click()
        elem = driver.find_element_by_css_selector("article h3")
        elem.click()
        assert "article-header" in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
