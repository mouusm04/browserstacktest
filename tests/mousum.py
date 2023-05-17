from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
driver = webdriver.Firefox()
driver.get('https://www.amazon.in/')
elem = driver.find_element(By.ID, "nav-link-accountList")
elem.click()
email = driver.find_element(By.ID, "ap_email")
email.send_keys('abc@gmail.com')
Continue_button = driver.find_element(By.ID, "continue")
Continue_button.submit()

password_textbox = driver.find_element(By.ID, "ap_password")
password_textbox.send_keys('password')

SignIn_button = driver.find_element(By.ID, "auth-signin-button-announce")
SignIn_button.submit()