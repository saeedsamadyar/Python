#Scenario Test Case

# Navigating to the https://ippanel.com/
# Open Website"https://ippanel.com/"
# import Username
# import Password
# clicking login 
# Add API Keys to the list 


#from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import keys

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install()) 
#import selenium webdriver()

driver.get("https://ippanel.com/")


username = driver.find_element('xpath', '//*[@id="txtUser"]')
username.send_keys("0090008030")
password = driver.find_element('xpath','//*[@id="txtPassword"]')
password.send_keys("Dsg@hd45645")

eli = driver.find_element('xpath','//*[@id="frmLogin"]/div[2]/button')
eli.click()

driver.quit()



