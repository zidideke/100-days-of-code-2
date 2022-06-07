
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("C:/Users/glady/Desktop/Web Development/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)

#driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# #print(article_count.text)
# article_count.click()

#portals=driver.find_element(By.LINK_TEXT, "all portals")
#portals.click()

#search = driver.find_element(By.NAME, "search")
# search.send_keys("alpacas")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Gladys")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Zi")
email = driver.find_element(By.NAME, "email")
email.send_keys("zi@yahoo.com")
sign_up_btn= driver.find_element(By.CLASS_NAME, "btn-block")
sign_up_btn.send_keys(Keys.ENTER)

