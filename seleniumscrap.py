import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait_time = 60
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
driver.get("http://45.77.40.141/toko")

# elem = driver.find_element_by_css_selector(".agile-login li:nth-child(2)").click()
#
# element = WebDriverWait(driver, wait_time).until(
#         EC.presence_of_element_located((By.NAME, "email"))
#     )
#
# element.send_keys("egi@egi.com")
#
# element = WebDriverWait(driver, wait_time).until(
#         EC.presence_of_element_located((By.NAME, "password"))
#     )
#
# element.send_keys("123")
#
# elem = driver.find_element_by_css_selector("form input[type='submit']").click()


data = driver.find_elements_by_css_selector('.categories ul li a')

i = 1
for d in range(0, len(data)):
    # title = d.find_element_by_css_selector('.snipcart-thumb > p').text
    # price = d.find_element_by_css_selector('.snipcart-thumb > h4').text
    # product.append({"title": title, "price": price})
    selector = f'.categories ul li:nth-of-type({i}) a'
    driver.find_element_by_css_selector(selector).click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    i += 1

driver.quit()
# print(product)

# elem = driver.find_element_by_css_selector(".col-md-9 .col-md-4 .snipcart-thumb > a").click()
#
# elem = driver.find_element_by_css_selector(".w3agile_description").text
#
# print(elem)
#
# elem = driver.execute_script("window.history.go(-1)")
