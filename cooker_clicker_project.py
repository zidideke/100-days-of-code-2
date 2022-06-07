from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
chrome_driver_path = Service("C:/Users/glady/Desktop/Web Development/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
#money = int(driver.find_element(By.CSS_SELECTOR, "#money").text)

buy_grandma= driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text
grandma_money=(int(buy_grandma.split()[2]))

buy_factory = driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text
factory_money=(int(buy_factory.split()[2]))

mine = driver.find_element(By.CSS_SELECTOR, "#buyMine b").text
mine_money=(mine.split()[2])


buy_shipment = driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text
shipment_money=(buy_shipment.split()[2])

portal=driver.find_element(By.CSS_SELECTOR, "#buyPortal b").text
portal_money=(portal.split()[2])


second=driver.find_element(By.CSS_SELECTOR, "#cps").text
seconds_count=(float(second.split()[2]))



# buy_time_machine=driver.find_element(By.CSS_SELECTOR, "#buyTime ").text
# time_machine_money=(buy_time_machine.split()[2])
# print(time_machine_money)
# buy_alchemy=driver.find_element(By.CSS_SELECTOR, "#buyAlchemylab b").text
# alchemy_money=(buy_alchemy.split()[2])
#print(alchemy_money)



# right_panel = driver.find_element(By.CSS_SELECTOR, "#rightPanel").text
# store = driver.find_element(By.CSS_SELECTOR, "#store").text
# print(store)
# for panel in right_panel:
#     if cookie_money >


while True:
    cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
    cookie.click()
    cookie_m = int(driver.find_element(By.CSS_SELECTOR, "#money").text)
    cookie_money=int(cookie_m)
    if cookie_money % 200 == 0:
        time.sleep(5)
        if seconds_count == :
            print(seconds_count)


# Cursor - 15
# Autoclicks every 5 seconds.
# Grandma - 100
# A nice grandma to bake more cookies.
# Factory - 500
# Produces large quantities of cookies.
# Mine - 2,000
# Mines out cookie dough and chocolate chips.
# Shipment - 7,000
# Brings in fresh cookies from the cookie planet.
# Alchemy lab - 50,000
# Turns gold into cookies!
# Portal - 1,000,000
# Opens a door to the Cookieverse.
# Time machine - 123,456,789
# Brings cookies from the past, before they were even eaten.




# driver = webdriver.Firefox()
# driver.get("http://somedomain/url_that_delays_loading")
#element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))

# wait = WebDriverWait(driver, 2)
# element = wait.until(EC.element_to_be_clickable((By.ID, '#cookie')))

# wait = WebDriverWait(driver, 2)
# element = wait.until(EC.element_to_be_clickable((By.ID, '#cookie')))


#

