
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source":
        "const newProto = navigator.__proto__;"
        "delete newProto.webdriver;"
        "navigator.__proto__ = newProto;"
    })
driver.get("https://www.delugerpg.com/")


print('testing')
driver.implicitly_wait(10)

up_arrow = driver.find_element_by_id("move_n")
down_arrow = driver.find_element_by_id("move_s")
for i in range(100):

    try:
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, "catch"))
        )
        element.click()
    except:
        try:
            #if i%2 == 0:
                element = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.ID, "move_n"))
                )
                element.click()
            #else:
                #element = WebDriverWait(driver, 2).until(
                    #EC.presence_of_element_located((By.ID, "move_s"))
                #)
                #element.click()
        except:
            print('oof')

