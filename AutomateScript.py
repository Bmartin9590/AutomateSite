#WAP that will automate an ecommerce website.
# The program should search for an item and add it to your cart. 

# To automate a website you have to first import selenium and the webdrivers and webdriver managers necessary for the browser your using.
# Also, you have to also import By so that you can direct your driver to find elements from the webpage
# "Import time" will also be needed so that we can control the duration of the webpage staying up so it doesn't close without finishing the task
# When your automating a website, you have to go to the webpage your automating and "inspect" the feautres your trying to engage and find a tag (id, class, css)
# Next, you use your driver and find_elements method to direct the automation.
# Along with this, you have to direct the automation on whether it should type (send.keys), click(mouse click) or other functions to accomplish the task
# Fianlly, you have to automate your driver to quit and close the webpage with driver.quit()
# The only limitation this code has is when you want to add the item to your cart, the website is dynamic and moves the element so the coordinates arent the same when you put in the XPATH

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.eastbay.com/")
driver.maximize_window()
time.sleep(5)

driver.refresh()
time.sleep(5)

search = driver.find_element(By.ID, "HeaderSearch_search_query").click()
search = driver.find_element(By.ID, "HeaderSearch_search_query").send_keys("football gloves")
time.sleep(5)
button = driver.find_element(By.CLASS_NAME, 'SearchForm-button')
button.click()
time.sleep(5)

product_link = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div/div[2]/div/div[2]/ul[1]/li[1]/div/a')
product_link.click()
time.sleep(5)

size_of_gloves = driver.find_element(By.XPATH,'//*[@id="ProductDetails"]/div[4]/fieldset/button[4]')
size_of_gloves.click()
time.sleep(10)

add_to_cart= driver.find_element(By.XPATH, '//*[@id="ProductDetails"]/ul/li[2]/button')
add_to_cart.click()
time.sleep(8)