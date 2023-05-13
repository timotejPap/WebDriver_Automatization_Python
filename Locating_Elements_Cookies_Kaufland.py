from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Toto ponechá okno otvorené
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

# Kódenie automatizácie
driver.get("https://www.kaufland.sk/")
driver.maximize_window()
time.sleep(3)

cookie = driver.find_element(By.XPATH, "//button[@id='402r8Hptk8']").click()
time.sleep(3)

cookie = driver.find_element(By.XPATH, "//button[contains(text(),'Povoliť vybrané')]").click()
time.sleep(3)

#kontakt = driver.find_element(By.CLASS_NAME, "m-navigation-corporate__link").click()

print("Nazov stranky je: ", driver.title)

linky = driver.find_elements("xpath", "//a[@href]")
for link in linky:
    if "byvanie" in link.get_attribute("innerHTML"):
        driver.get(link.get_attribute("href"))
        break
print(linky)
"""
postele = driver.find_elements(By.XPATH, "//div[contains(@class, 'rd-category-tiles')][.//a@href")

for nabytok in postele:
    print(nabytok.get_attribute("innerHTML"))
"""