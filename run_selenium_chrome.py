from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\\browser_drivers\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://selenium.dev")
driver.get("https://www.youtube.com/watch?v=VSDWqbc8wig&list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz&index=9")
driver.close()

firefox_service = Service("C:\\browser_drivers\\geckodriver-v0.34.0-win64\\geckodriver.exe")
firefox_driver = webdriver.Firefox(service=firefox_service)
firefox_driver.get("http://selenium.dev")
firefox_driver.close()

edge_driver = Service("C:\\browser_drivers\\edgedriver_win64\\msedgedriver.exe")
edge_driver = webdriver.Edge(service=edge_driver)
edge_driver.get("http://selenium.dev")
edge_driver.close()



