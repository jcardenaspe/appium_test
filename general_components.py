from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Constants as Cons


class general_components:

    def close_alert(driver):
        driver.switch_to.alert.accept()

    def create_contact(driver, contact_name, phone_number):
        print("Test add a new contact")
        driver.find_element_by_id("addContactButton").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contactNameEditText")))
        driver.find_element_by_id("contactNameEditText").send_keys(contact_name)
        driver.find_element_by_id("contactPhoneEditText").send_keys(phone_number)
        driver.find_element_by_id("contactEmailEditText").send_keys(Cons.CONTACT_EMAIL)
        driver.find_element_by_id("contactSaveButton").click()

    def get_list_of_contacts(driver):
        contact_text_list = []
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "contactList")))
        contact_elements = driver.find_elements_by_xpath('//android.widget.TextView[@content-desc="false"]')
        print(str(len(contact_elements)))
        for contact in contact_elements:
            contact_text_list.append(contact.text)
        return contact_text_list
