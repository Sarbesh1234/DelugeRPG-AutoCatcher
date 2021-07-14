
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
#up_arrow = driver.find_element_by_id("move_n")
#down_arrow = driver.find_element_by_id("move_s")
print('testing')
driver.implicitly_wait(5)
driver.find_element_by_name('username').send_keys('pokevortex')
driver.find_element_by_name('password').send_keys('azmarcos123')
driver.find_element_by_name('Login').click()
driver.implicitly_wait(10)
'''for i in range(1000):

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
    #try:
        #element = WebDriverWait(driver, 2).until(
        #EC.presence_of_element_located((By.ID, "move_s"))
        #)
       #element.click()
    #except:
        #print('no work')

        try:
        #element = WebDriverWait(driver, 2).until(
            #EC.presence_of_element_located((By.CSS_SELECTOR, "input[class='btn-catch-button']"))
        #)
        #element.click()
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div[2]/form/input[4]').click()
        print('goes in button')
    except:
        print('no work')
'''
j = 0
for i in range(1000):

    while True:
        try:
            print('entered')
            #driver.find_element_by_id('catch').click()
            #Try to catch button
            driver.find_element_by_class_name('btn-catch-action').click()
            print('got through without exception')
            break;
        except:
            if j % 2 == 0:
                #up arrow
                driver.find_element_by_id('move_n').click()
            else:
                #down arrow
                driver.find_element_by_id('move_s').click()
            print('fail')
        j += 1
    driver.implicitly_wait(5)
    #scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(5)
    #click button
    driver.find_element_by_class_name('btn-battle-action').click()
    driver.implicitly_wait(5)
    #scroll midway
    driver.execute_script("window.scrollTo(0, 500);")
    driver.implicitly_wait(5)

    try:
        driver.find_elements_by_name('useitem_').click()
    except :
        driver.find_element_by_name('useitem_').click()
    driver.implicitly_wait(5)
    driver.back()
    driver.implicitly_wait(5)
    '''
    try:
        driver.find_element_by_class_name('btn-battle-action').click()
    except:
        driver.find_element_by_class_name('btn-battle-action').click()

    driver.implicitly_wait(5)
    try:
        driver.find_element_by_class_name('btn btn-primary').click()
        #driver.find_element_by_link_text('Return To Map.')
    except:
        driver.find_element_by_class_name('btn btn-primary').click()
        #driver.find_element_by_link_text('Return To Map.')
    driver.implicitly_wait(2)
    print('bruh did you click or not')
    '''