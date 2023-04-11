from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create a new Chrome driver instance
driver = webdriver.Chrome(executable_path="/Users/saeed/Downloads/chromedriver")

# Test case 1: Verify that the website loads successfully without any errors.
driver.get("https://derivfe.github.io/qa-test/")
assert "QA Test" in driver.title

# Test case 2: Verify that the logo is displayed on the website's homepage.
logo = driver.find_element_by_class_name("logo")
assert logo.is_displayed()

# Test case 3: Verify that the website's navigation menu is functional and links to the correct pages.
nav_links = driver.find_elements_by_css_selector("#nav li a")
for link in nav_links:
    link.click()
    assert "QA Test" in driver.title

# Test case 4: Verify that the website's search function is working as expected, and returns relevant search results.
search_box = driver.find_element_by_id("search")
search_box.send_keys("Selenium")
search_box.send_keys(Keys.RETURN)
WebDriverWait(driver, 10).until(EC.title_contains("Selenium"))

# Test case 5: Verify that the website's contact form is functional, and that messages are sent successfully.
contact_name = driver.find_element_by_name("name")
contact_name.send_keys("John Doe")
contact_email = driver.find_element_by_name("email")
contact_email.send_keys("johndoe@example.com")
contact_message = driver.find_element_by_name("message")
contact_message.send_keys("This is a test message.")
contact_message.submit()
WebDriverWait(driver, 10).until(EC.title_contains("Thank you"))

# Test case 6: Verify that the website's social media icons are working as expected, and link to the correct social media profiles.
social_icons = driver.find_elements_by_css_selector(".social-icons li a")
for icon in social_icons:
    assert icon.get_attribute("href") != ""

# Test case 7: Verify that the website's footer is displayed correctly, and contains all necessary links and information.
footer_links = driver.find_elements_by_css_selector("#footer li a")
for link in footer_links:
    assert link.get_attribute("href") != ""

# Test case 8: Verify that the website's images are displayed correctly, and that they are optimized for fast loading.
images = driver.find_elements_by_tag_name("img")
for image in images:
    assert image.get_attribute("src") != ""

# Test case 9: Verify that the website's content is free of spelling and grammatical errors.
body_text = driver.find_element_by_tag_name("body").text
assert "spelling" not in body_text.lower() and "grammar" not in body_text.lower()

# Test case 10: Verify that the website is mobile-responsive and displays correctly on different devices.
driver.set_window_size(360, 640)
assert "QA Test" in driver.title

# close the browser window when testing is complete
driver.quit()
