from selenium import webdriver

def first_test():
    driver = webdriver.chrome()
    driver.maximize_windows()
    driver.get("https://translate.google.com/?hl=en&tab=wT")
    print("title: ", driver.tile)
