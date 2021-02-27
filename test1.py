from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.cdv.pl")
driver.close()