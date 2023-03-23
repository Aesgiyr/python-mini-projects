from selenium.webdriver.common.by import By # Bunu mutlaka importla
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
username=input("Username: ")
password=input("Password: ")
driver = webdriver.Safari()
url = "https://github.com"
driver.get(url)
time.sleep(1)
driver.maximize_window()
time.sleep(1)
signButton = driver.find_element(By.XPATH ,"/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a")
signButton.click()
time.sleep(1)
usernameScreen = driver.find_element(By.XPATH, '//*[@id="login_field"]')
usernameScreen.send_keys(username)
time.sleep(1)
passwordScreen = driver.find_element(By.XPATH, '//*[@id="password"]')
passwordScreen.send_keys(password)
time.sleep(1)
signInButton = driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[11]')
passwordScreen.send_keys(Keys.ENTER)
time.sleep(5)
driver.close