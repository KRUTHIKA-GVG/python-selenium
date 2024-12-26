from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get("https://www.yatra.com/")
list_a = driver.find_elements(By.TAG_NAME, "a")
print(len(list_a))

for i in list_a:
    print(i.text)

list_input = driver.find_elements(By.TAG_NAME, "input")
print(len(list_input))


