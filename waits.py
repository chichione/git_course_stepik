from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, os, math


try: 
 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    
    #confirm
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, 'book')
    button.click()
 

    #calc
    def calc(x):
    	return str(math.log(abs(12*math.sin(int(x)))))
 
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    print(y)
    space = browser.find_element(By.CSS_SELECTOR, "#answer")
    space.send_keys(y) 

   
    #Submit
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    
    
