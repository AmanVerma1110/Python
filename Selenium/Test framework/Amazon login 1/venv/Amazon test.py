import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")
driver.implicitly_wait(5)

driver.find_element(By.XPATH,(".//a[@data-nav-role='signin']")).click()
driver.find_element(By.XPATH,("//input[@type='email']")).send_keys(8448786695)
driver.find_element(By.XPATH,("//input[@id='continue']")).click()
driver.find_element(By.XPATH,("//input[@type='password']")).send_keys("Test12345")
driver.find_element(By.XPATH,("//input[@id='signInSubmit']")).click()
driver.find_element(By.XPATH,("//*[@id='twotabsearchtextbox']")).send_keys("Laptop")


print(driver.title)

driver.quit()

