# gmail_login_flow
# If you do not want to display, uncomment and rewrite


# from selenium.webdriver import Firefox, FirefoxOptions
from selenium import webdriver
import time
# options = FirefoxOptions()
# options.add_argument('-headless')

url = "https://mail.google.com/mail/u/0/#inbox"

# browser = Firefox(options=options)

browser = webdriver.Firefox()
browser.get(url)

mail_address = ""
address_box = browser.find_element_by_id("identifierId")
next_btn = browser.find_element_by_class_name("CwaK9")
address_box.clear()
address_box.send_keys(mail_address)
next_btn.click()

time.sleep(5)
passwd = ""
pass_box = browser.find_element_by_name("password")
next_btn_pass = browser.find_element_by_class_name("RveJvd")
pass_box.clear()
pass_box.send_keys(passwd)
next_btn_pass.click()
