from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
driver.maximize_window()
driver.find_element(By.ID, "login-input").send_keys("test@test.com")
driver.find_element(By.NAME, "login-input").clear()


driver.find_element(By.NAME, "login-input").send_keys("test1@test.com")
driver.find_element(By.NAME, "login-input").clear()


driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys("test2@test.com")
driver.find_element(By.NAME, "login-input").clear()


driver.find_element(By.CSS_SELECTOR, "input[id='login-input']").send_keys("test3@test.com")
driver.find_element(By.NAME, "login-input").clear()


driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys("test4@test.com")
time.sleep(5)

driver.get("https://www.yatra.com/")
driver.find_element(By.LINK_TEXT, "For Business").click()
sleep(5)

driver.get("https://www.yatra.com/")
driver.find_element(By.PARTIAL_LINK_TEXT, "Business").click()
sleep(5)

driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
driver.find_element(By.TAG_NAME, "input").send_keys("abc@gmail.com")
sleep(5)

driver.find_element(By.CLASS_NAME, "email-login-box").clear()
driver.find_element(By.CLASS_NAME, "email-login-box").send_keys("def@gmail.com")
sleep(5)

driver.find_element(By.CSS_SELECTOR, ".email-login-box").clear()
driver.find_element(By.CSS_SELECTOR, ".email-login-box").send_keys("hij@gmail.com")
sleep(5)

driver.close()
