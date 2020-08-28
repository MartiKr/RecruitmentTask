import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

company = "Company"
email = "email@email.com"
full_name = "Imię nazwisko"
country_phone_code = "(+30) Grecja"
tel = 123456789
password = "abcdefgh"

success_mesage = "OK - some registration logic is mocked"

path_d = os.getcwd() + r'\chromedriver.exe'
url = r"https://dev-1.clicktrans.pl/register-test/courier"

#go to the website with registry form
wd = webdriver.Chrome(executable_path=path_d)
wd.get(url)

def find_element(id, value):
    element = wd.find_element_by_id(id)
    element.send_keys(value)

#fill company name textbox
find_element("user_register_company_name", company)

#fill email textbox
find_element("user_register_email", email)

#fill the first and the last name textbox
find_element("user_register_name", full_name)

#select correct country phone code textbox
phone_code = wd.find_element_by_id("user_register_phoneCode")
drp_phone_code = Select(phone_code)
drp_phone_code.select_by_visible_text(country_phone_code)

#fill the phone number textbox
find_element("user_register_phone", tel)

#fill the password textbox
find_element("user_register_plainPassword", password)

#select all check boxes
def click_checkbox(id):
    wd.find_element_by_id(id).click()

click_checkbox("user_register_settings_agreementRegulations")
click_checkbox("user_register_settings_agreementPersonalData")
click_checkbox("user_register_settings_agreementMarketing")

#click "Zarejestruj"
reg = wd.find_element_by_id("user_register_submit").click()


try:
    #wait for sending registration form
    element = WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]")))
    success = wd.find_element_by_xpath("/html/body/div[6]/div").text

    #chceck if success mesage is correct
    assert success == success_mesage

finally:
    #quit browser
    wd.quit()
