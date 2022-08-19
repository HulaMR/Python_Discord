from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
import string


def password_generation():
    low = string.ascii_lowercase
    up = string.ascii_uppercase
    dig = string.digits
    full = low + up + dig

    return "".join(random.sample(full, 8))


email = input("Email: ")
username = input("Username: ")
password = password_generation()
print("Password: " + password)

driver = webdriver.Chrome("chromedriver")

driver.get("https://discord.com/register")

# Register
driver.find_element('name', "email").send_keys(email)
driver.find_element('name', "username").send_keys(username)
driver.find_element('name', "password").send_keys(password)
driver.find_element(By.XPATH, ".//div[@tabindex=1]").click()
driver.find_element(By.XPATH, './/div[@id="react-select-2-option-0"]').click()
driver.find_element(By.XPATH, ".//div[@tabindex=2]").click()
driver.find_element(By.XPATH, './/div[@id="react-select-3-option-0"]').click()
driver.find_element(By.XPATH, ".//div[@tabindex=3]").click()
driver.find_element(By.XPATH, './/div[@id="react-select-4-option-40"]').click()
driver.find_element(By.XPATH,
                    './/button[@class="button-1cRKG6 button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeLarge-3mScP9 fullWidth-fJIsjq grow-2sR_-F"]').click()


# ReCaptcha
def RC():
    rc = input("Waiting[skip]:")
    if rc == "skip":
        pass
    else:
        RC()


RC()
driver.get("https://discord.com/login")
sleep(10)
driver.find_element('name', "email").send_keys(email)
driver.find_element('name', "password").send_keys(password)
sleep(10)
driver.find_element(By.XPATH,
                    './/button[@class="marginBottom8-emkd0_ button-1cRKG6 button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeLarge-3mScP9 fullWidth-fJIsjq grow-2sR_-F"]').click()

driver.get("https://discord.com/channels/@me")


url = "https://discord.com/channels/@me"
response = requests.get(url)
print(response.request.headers)
