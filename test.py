import unittest
import os
import Constants as cons
import general_components as gc
from appium import webdriver
import sys


class ContactManagerAPP(unittest.TestCase):
    "Class to run tests against the Chess Free app"

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'HUAWEI P smart 2019'
        desired_caps['udid'] = 'VMM4C19219000494'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['app'] = os.path.join(os.path.dirname(__file__),(cons.APK_PATH))
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = '.ContactManager'
        desired_caps['uiautomator2ServerLaunchTimeout'] = 100000
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_installation(self):
        print("Test the app installation")
        if self.assertTrue(self.driver.is_app_installed(cons.APP_PACKAGE)):
            self.driver.remove_app(cons.APP_PACKAGE)
        self.driver.install_app(cons.APK_PATH)
        self.assertTrue(self.driver.is_app_installed(cons.APP_PACKAGE))
        gc.general_components.close_alert(self.driver)

    def test_contact_list(self):
        print("Test the contact list")
        gc.general_components.close_alert(self.driver)
        self.assertGreater(len(self.driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout")), 0)

    def test_add_contact_button_displayed(self):
        print("Test if add contact button is displayed")
        gc.general_components.close_alert(self.driver)
        self.assertTrue(self.driver.find_element_by_id("addContactButton").is_displayed())

    def test_created_contact(self):
        print("Test if the contact was created")
        gc.general_components.close_alert(self.driver)
        gc.general_components.create_contact(self.driver, sys.argv[1], sys.argv[2])
        self.assertTrue(sys.argv[1] in gc.general_components.get_list_of_contacts(self.driver))


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ContactManagerAPP("test_installation"))
    suite.addTest(ContactManagerAPP("test_contact_list"))
    suite.addTest(ContactManagerAPP("test_add_contact_button_displayed"))
    suite.addTest(ContactManagerAPP("test_created_contact"))
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite)
