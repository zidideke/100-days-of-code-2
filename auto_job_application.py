from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
import time

chrome_driver_path = Service("C:/Users/glady/Desktop/Web Development/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&keywords=software%20developer")
MY_PHONE_NUMBER="12444444446"
time.sleep(5)

sign_in= driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

username= driver.find_element(By.ID, "username")
username.send_keys("zi.gladysoro@gmail.com")
password = driver.find_element(By.ID, "password")
password.send_keys("#1Zionlady")
sign_in= driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()


time.sleep(2)



easy_apply_btn= driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
easy_apply_btn.click()
phone_number = driver.find_element(By.NAME, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3095018407,57049925,phoneNumber~nationalNumber)')
phone_number.send_keys("12345677")


next_button = driver.find_element(By.CLASS_NAME,"artdeco-button")
next_button.click()

next_btn = driver.find_element(By.CLASS_NAME, 'display-flex button')
next_btn.click()
time.sleep(2)

cross_button= driver.find_element(By.CLASS_NAME, 'artdeco-button')
cross_button.click()
time.sleep(2)

discard_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[3]/button[2]')
discard_button.click()

# all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
#
# for listing in all_listings:
#     print("called")
#     listing.click()
#     time.sleep(2)
#
#     # Try to locate the apply button, if can't locate then skip the job.
#     try:
#         apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
#         apply_button.click()
#         time.sleep(5)
#
#         # If phone field is empty, then fill your phone number.
#         phone = driver.find_element_by_class_name("fb-single-line-text__input")
#         if phone.text == "":
#             phone.send_keys(PHONE)
#
#         submit_button = driver.find_element_by_css_selector("footer button")
#
#         # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
#             close_button.click()
#             time.sleep(2)
#             discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
#             discard_button.click()
#             print("Complex application, skipped.")
#             continue
#         else:
#             submit_button.click()
#
#         # Once application completed, close the pop-up window.
#         time.sleep(2)
#         close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
#         close_button.click()
#
#     # If already applied to job or job is no longer accepting applications, then skip.
#     except NoSuchElementException:
#         print("No application button, skipped.")
#         continue
#
# time.sleep(5)
# driver.quit()