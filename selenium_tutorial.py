
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("C:/Users/glady/Desktop/Web Development/chromedriver")
#driver = webdriver.Chrome(executable_path=chrome_driver_path)
#driver.get("http://www.amazon.com")


#s = Service('C:/Users/.../chromedriver.exe')
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.python.org/")

# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget name")
# for name in event_names:
#     print(name.text)

event_times =driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')
event_names =driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')
# for name in event_names:
#     print(name.text)

events={}

for n in range(len(event_times)):
    events[n] = {
       "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)


driver.quit()
