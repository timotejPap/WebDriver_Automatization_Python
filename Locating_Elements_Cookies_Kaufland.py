from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Toto ponechá okno otvorené
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.maximize_window()

# Kódenie automatizácie
driver.get("https://www.kaufland.sk/")
driver.maximize_window()
time.sleep(3)

cookie = driver.find_element(By.XPATH, "//button[@id='402r8Hptk8']").click()
time.sleep(3)

cookie = driver.find_element(By.XPATH, "//button[contains(text(),'Povoliť vybrané')]").click()
time.sleep(3)
print("Nazov stranky je: ", driver.title)

search = driver.find_element(By.NAME, "search_value")
time.sleep(5)
submit = driver.find_element(By.XPATH, "//button[@type='button']//span[@class='svg-icon']//*[name()='svg']")
ActionChains(driver).send_keys_to_element(search, "slanina").click(submit).perform()
time.sleep(4)
slane = driver.find_element(By.XPATH, "//div[contains(text(),'Slané pečivo')]").click()
#link = driver.find_element(By.LINK_TEXT, "Kariéra v predajniach Kaufland").click()